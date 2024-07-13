import aws_cdk as core
import aws_cdk.assertions as assertions

from cdk_recon.cdk_recon_stack import CdkReconStack

# example tests. To run these tests, uncomment this file along with the example
# resource in cdk_recon/cdk_recon_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = CdkReconStack(app, "cdk-recon")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
