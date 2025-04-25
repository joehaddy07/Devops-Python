# Define the AWS provider
provider "aws" {
  region = "us-east-1"
}
# Create a Lambda function
resource "aws_lambda_function" "DIT" {
  function_name = "DIT"
  role          = aws_iam_role.lambda_role.arn
  handler       = "hello-python.lambda_handler"
  runtime       = "python3.8"
  # Use a zip file as the source code
  filename      = "${path.module}/python/hello-python.zip"
}
# Create an IAM role for the Lambda function
resource "aws_iam_role" "lambda_role" {
  name = "lambda_role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "lambda.amazonaws.com"
        }
      },
    ]
  })
}
# Attach the AWSLambdaBasicExecutionRole policy to the role
resource "aws_iam_role_policy_attachment" "DIT_role" {
  role       = aws_iam_role.DIT_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}
# Create an API Gateway REST API
resource "aws_api_gateway_rest_api" "DIT_api" {
  name        = "DIT_api"
  description = "An DIT_api API Gateway that invokes a Lambda function"
}
# Create a resource for the API
resource "aws_api_gateway_resource" "DIT_api" {
  rest_api_id = aws_api_gateway_rest_api.DIT_api.id
  parent_id   = aws_api_gateway_rest_api.DIT_api.root_resource_id
  path_part   = "{proxy+}"
}
# Create a method for the resource
resource "aws_api_gateway_method" "DIT_api" {
  rest_api_id   = aws_api_gateway_rest_api.DIT_api.id
  resource_id   = aws_api_gateway_resource.DIT_api.id
  http_method   = "ANY"
  authorization = "NONE"
}
# Create an integration for the method
resource "aws_api_gateway_integration" "DIT_api" {
  rest_api_id             = aws_api_gateway_rest_api.DIT_api.id
  resource_id             = aws_api_gateway_resource.DIT_api.id
  http_method             = aws_api_gateway_method.DIT_api.http_method
  integration_http_method = "POST"
  type                    = "AWS_PROXY"
  uri                     = aws_lambda_function.DIT.invoke_arn
}
# Create a deployment for the API
resource "aws_api_gateway_deployment" "DIT_api" {
  depends_on = [
    aws_api_gateway_integration.DIT_api,
  ]
  rest_api_id       = aws_api_gateway_rest_api.DIT_api.id
  stage_name        = "test"
}
# Create a permission for the API to invoke the Lambda function
resource "aws_lambda_permission" "DIT_permission" {
  statement_id  = "AllowExecutionFromAPIGateway"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.DIT.function_name
  principal     = "apigateway.amazonaws.com"
  # The /*/* part allows invocation from any method on any resource path within the API Gateway REST API.
  source_arn    = "${aws_api_gateway_rest_api.DIT_api.execution_arn}/*/*"
}