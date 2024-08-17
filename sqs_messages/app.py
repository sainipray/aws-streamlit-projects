import streamlit as st

from .design import styled_header, styled_subheader, divider
from .logic import create_queue, send_message, receive_messages, delete_queue, delete_message, list_queues


def main():
    st.title("SQS Manager")

    st.sidebar.title("SQS Operations")
    operation = st.sidebar.radio("Choose an operation", [
        "List Queues", "Create Queue", "Send Message", "Receive Messages", "Delete Queue"])

    if operation == "List Queues":
        styled_header("List All Queues")
        queues = list_queues()
        if queues:
            for queue_url in queues:
                cols = st.columns([4, 1])
                with cols[0]:
                    st.write(f"- {queue_url}")
                with cols[1]:
                    if st.button(f"Delete Queue", key=queue_url):
                        delete_queue(queue_url)
                        st.success(f"Queue with URL {queue_url} deleted.")
        else:
            st.write("No queues available.")

    elif operation == "Create Queue":
        styled_header("Create a Queue")
        styled_subheader("Specify the queue name below:")
        queue_name = st.text_input("Queue Name")
        if st.button("Create Queue"):
            if queue_name:
                queue_url = create_queue(queue_name)
                st.success(f"Queue created successfully. Queue URL: {queue_url}")
            else:
                st.warning("Queue name cannot be empty.")
        divider()

    elif operation == "Send Message":
        styled_header("Send a Message")
        styled_subheader("Provide the queue URL and message body:")
        queue_url = st.text_input("Queue URL")
        message_body = st.text_area("Message Body")
        if st.button("Send Message"):
            if queue_url and message_body:
                message_id = send_message(queue_url, message_body)
                st.success(f"Message sent with ID: {message_id}")
            else:
                st.warning("Queue URL and message body cannot be empty.")
        divider()

    elif operation == "Receive Messages":
        styled_header("Receive Messages")
        styled_subheader("Enter the queue URL to retrieve messages:")
        queue_url = st.text_input("Queue URL")
        if st.button("Receive Messages"):
            if queue_url:
                messages = receive_messages(queue_url)
                if messages:
                    for message in messages:
                        st.write(f"**Message ID:** {message['MessageId']}")
                        st.write(f"**Body:** {message['Body']}")
                        st.write(f"**Receipt Handle:** {message['ReceiptHandle']}")
                        if st.button(f"Delete Message {message['MessageId']}", key=message['MessageId']):
                            delete_message(queue_url, message['ReceiptHandle'])
                            st.success(f"Message with ID {message['MessageId']} deleted.")
                        st.write("---")
                else:
                    st.write("No messages available.")
            else:
                st.warning("Queue URL cannot be empty.")
        divider()

    elif operation == "Delete Queue":
        styled_header("Delete a Queue")
        styled_subheader("Provide the queue URL to delete:")
        queue_url = st.text_input("Queue URL")
        if st.button("Delete Queue"):
            if queue_url:
                delete_queue(queue_url)
                st.success(f"Queue with URL {queue_url} deleted.")
            else:
                st.warning("Queue URL cannot be empty.")
        divider()
