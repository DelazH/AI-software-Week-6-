Task 1: Edge AI Prototype

Dataset: TrashNet (6 classes: glass, paper, metal, etc.)

Tech Stack: TensorFlow Lite in Colab → Raspberry Pi simulator

Model Architecture:

model = Sequential([
  Conv2D(32, (3,3), activation='relu', input_shape=(224,224,3)),
  MaxPooling2D(2,2),
  Flatten(),
  Dense(128, activation='relu'),
  Dense(6, activation='softmax')  # TrashNet classes
])
Key Metric: Target >85% accuracy with <5ms inference time on Raspberry Pi

Deployment Benefit: Zero-network waste sorting robots in remote areas

Task 2: Smart Agriculture IoT

Sensors: Soil moisture (capacitive), Temperature/Humidity (DHT22), Multispectral cameras (NDVI)

AI Model: Random Forest Regressor for yield prediction (handles mixed crop data)

Data Flow Diagram:
graph TD
  A[Sensors] --> B(Edge Gateway)
  B --> C[Data Preprocessing]
  C --> D{Random Forest Model}
  D --> E[Yield Prediction]
  E --> F[Irrigation Control System]
  D --> G[Farmer Dashboard]
Proposal Focus: Drought prediction using historical weather embeddings

Task 3: Personalized Medicine Bias

Bias Analysis: TCGA data underrepresents rural populations → AI overfits to urban genomic profiles

Systemic Solution:

Partner with community health centers for diverse sample collection

Federated Learning to train models without raw data transfer

Policy mandate for "bias stress tests" before clinical deployment
