


from transformers import ResNetConfig, ResNetModel


def get_resnet_model(model_name="microsoft/resnet-50"):
    model = ResNetModel.from_pretrained(model_name)

    return model

