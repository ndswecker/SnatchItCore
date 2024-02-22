
# SnatchItAPI

Welcome to SnatchItAPI, a cutting-edge C# .NET Core 8 Web API designed specifically for bird banders adhering to the Micro Aging protocol. Our API facilitates the seamless submission of data and photos to a cloud-based database, streamlining the process of tracking and managing bird banding records.

## Features

SnatchItAPI offers a comprehensive suite of features to support bird banders, including:

- **User Registration**: Allows new banders to register and join the community.
- **Authentication and Authorization**: Secure login process with JWTs (JSON Web Tokens) to ensure data security and integrity.
- **Bander Information Management**: Easy management and updating of bander profiles and credentials.
- **Data Record Uploads**: Facilitates the upload of bird banding data records to a centralized cloud database.
- **Record Viewing**: Enables users to view their submitted records in the database, enhancing data accessibility and usability.

## Getting Started

### Prerequisites

Before you begin, ensure you have the latest version of .NET Core (8.0) installed on your machine. If you need to install it, visit the [official .NET Core download page](https://dotnet.microsoft.com/download/dotnet/8.0).

### Installation

1. Clone the repository to your local machine:
   ```sh
   git clone https://github.com/yourusername/SnatchItAPI.git

### Building & the Application

1. To build the SnatchItAPI for release, use the following command in your command line or terminal:
   ```sh
   dotnet build --configuration Release
2. After building the application, you can deploy it to Azure using the Azure CLI. Change the name to something other than mine. If you haven't already, install the Azure CLI by following the instructions on the official Azure CLI documentation page.With the Azure CLI installed, navigate to your project directory and execute the following command in the Azure Command Prompt:
   ```sh
   az webapp up --sku F1 --name SnatchItAPI --os-type linux