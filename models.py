import torch.nn as nn


class Perceptron(nn.Module):
    """
    A PyTorch implementation of a single-layer perceptron neural network.
    https://www.javatpoint.com/single-layer-perceptron-in-tensorflow
    """

    def __init__(self, input_size, output_size):
        super(Perceptron, self).__init__()

        self.fc = nn.Linear(input_size, output_size)
        self.sigmoid = nn.Sigmoid()

    def forward(self, inputs):
        output = self.fc(inputs)
        # large large can lead to nan for sigmoid function. so, clip large value
        # clampted_output = torch.clamp(output, min=-10, max=10)
        output = self.sigmoid(output)

        return output.squeeze()
