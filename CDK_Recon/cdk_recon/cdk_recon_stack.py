from aws_cdk import (
    Duration,
    Stack,
    aws_lambda as _lambda,
    aws_lambda_python_alpha as _alambda,
    aws_events as events,
    aws_events_targets as targets,
    aws_ec2 as ec2,
    aws_iam as iam,
)
from constructs import Construct

class CdkReconStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # Retrieve the environment context
        env_context = self.node.try_get_context("env")

        if not env_context:
            raise ValueError("Environment context 'env' is not set")
        
        # Load environment specific configuration from cdk.json
        config = self.node.try_get_context("envs")[env_context]

        if not config:
            raise ValueError(f"Configuration for environment '{env_context}' is not found")
        
        # Define the IAM role
        iam_role_arn = config.get("iam_role_arn")
        #lambda_role = iam.Role.from_role_arn(self, "LambdaRole", role_arn=iam_role_arn)

        # Lambda function
        recon_lambda = _alambda.PythonFunction(
            self, "ReconFunction",
            entry="./reconciliation/",
            runtime=_lambda.Runtime.PYTHON_3_9,
            index='lambda_function.py',
            handler="lambda_handler",
            environment={
                "secret_name": config["secret_name"],
                "sql_server": config["sql_server"],
                "sql_database": config["sql_database"]
            },
            #role=lambda_role
        )

        # CloudWatch Events Rule
        recon_rule = events.Rule(
            self, "ReconRule",
            schedule=events.Schedule.cron(hour="14", minute="00")
        )
        recon_rule.add_target(targets.LambdaFunction(recon_lambda))


