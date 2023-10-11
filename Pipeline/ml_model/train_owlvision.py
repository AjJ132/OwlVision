import torch
import torch.nn as nn
import torch.optim as optim

class PotentialTicketHolderNN(nn.Module):
    def __init__(self, input_dim):
        super(PotentialTicketHolderNN, self).__init__()
        
        # Define the layers
        self.fc1 = nn.Linear(input_dim, 128)   # Change 128 to any desired number of neurons in hidden layer
        self.fc2 = nn.Linear(128, 64)         # Change 64 to any desired number of neurons in 2nd hidden layer
        self.fc3 = nn.Linear(64, 1)

        # Define activation functions
        self.relu = nn.ReLU()
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        x = self.fc1(x)
        x = self.relu(x)
        x = self.fc2(x)
        x = self.relu(x)
        x = self.fc3(x)
        x = self.sigmoid(x)
        return x

# Example usage
input_dim = 10  # This should be equal to the number of features in your dataset
model = PotentialTicketHolderNN(input_dim)
criterion = nn.BCELoss()  # Binary Cross-Entropy loss
optimizer = optim.Adam(model.parameters())
