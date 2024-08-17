import json
import os

import streamlit as st

from .design import styled_header, styled_subheader, divider
from .logic import create_lambda_function, list_lambda_functions, delete_lambda_function, invoke_lambda_function, \
    get_role_arn


def main():
    st.title("AWS Lambda Manager")

    st.sidebar.title("Lambda Operations")
    operation = st.sidebar.radio("Choose an operation", [
        "List Functions", "Create Function", "Invoke Function", "Delete Function"])

    if operation == "List Functions":
        styled_header("List All Lambda Functions")
        functions = list_lambda_functions()
        if 'error' in functions:
            st.error(functions['error'])
        elif functions:
            for function in functions:
                st.write(f"- {function['FunctionName']}")
                if st.button(f"Delete Function {function['FunctionName']}"):
                    result = delete_lambda_function(function['FunctionName'])
                    if 'error' in result:
                        st.error(result['error'])
                    else:
                        st.success(result['status'])
        else:
            st.write("No functions available.")
        divider()

    elif operation == "Create Function":
        arn = get_role_arn(os.environ['IAM_ROLE_NAME'])
        styled_header("Create Lambda Function")
        styled_subheader("Provide function details:")
        function_name = st.text_input("Function Name")
        runtime = st.selectbox("Runtime", ["python3.8", "python3.9", "python3.10"])
        role_arn = st.text_input("Role ARN", value=arn)
        handler = st.text_input("Handler (e.g., lambda_function.lambda_handler)", value='lambda_function.lambda_handler')
        code_string = st.text_area("Lambda Function Code (Python)")
        if st.button("Create Function"):
            if function_name and runtime and role_arn and handler and code_string:
                result = create_lambda_function(function_name, runtime, role_arn, handler, code_string)
                if 'error' in result:
                    st.error(result['error'])
                else:
                    st.success("Function created successfully.")
        divider()

    elif operation == "Invoke Function":
        styled_header("Invoke Lambda Function")
        styled_subheader("Provide function name and payload:")
        function_name = st.text_input("Function Name")
        payload_input = st.text_area("Payload (JSON format)")
        if st.button("Invoke Function"):
            if function_name and payload_input:
                try:
                    payload = json.loads(payload_input)
                    result = invoke_lambda_function(function_name, payload)
                    st.json(result)
                except json.JSONDecodeError:
                    st.error("Invalid JSON format in payload.")
        divider()

    elif operation == "Delete Function":
        styled_header("Delete Lambda Function")
        styled_subheader("Provide the function name to delete:")
        function_name = st.text_input("Function Name")
        if st.button("Delete Function"):
            if function_name:
                result = delete_lambda_function(function_name)
                if 'error' in result:
                    st.error(result['error'])
                else:
                    st.success(result['status'])
        divider()
