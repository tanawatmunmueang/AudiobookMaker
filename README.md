# AudiobookMaker

### Installation Tutorial

#### 1. Install python, I am using Python 3.12.10 (https://www.python.org/downloads/release/python-31210/)

#### 2. Clone the GitHub Repository:
```bash
git clone https://github.com/tanawatmunmueang/AudiobookMaker.git

cd AudiobookMaker
```
#### 3. Create a Python Virtual Environment:
```bash
python -m venv myenv
```
This command creates a new Python virtual environment named `myenv` for isolating dependencies.

#### 4. Activate the Virtual Environment:
- **For Windows:**
  ```bash
  myenv\Scripts\activate
  ```
- **For Linux:**
  ```bash
  source myenv/bin/activate
  ```
This activates the virtual environment, enabling you to install and run dependencies in an isolated environment.
Here’s the corrected version of point 4, with proper indentation for the subpoints:

#### 5. Upgrade pip
```bash
python -m pip install --upgrade pip
```

#### 6. Install Kokoro TTS
```bash
pip install git+https://github.com/hexgrad/kokoro.git
```

#### 7. Install PyTorch:

- **For GPU (CUDA-enabled installation):**
  - Check CUDA Version (for GPU setup):
    ```bash
    nvcc --version
    ```
    Find your CUDA version example ```11.8```

  - Visit [PyTorch Get Started](https://pytorch.org/get-started/locally/) and install the version compatible with your CUDA setup.:<br>
    - For CUDA 11.8 (If you have issues installing another version then install this one):
    ```
    pip install torch  --index-url https://download.pytorch.org/whl/cu118
    ```
    - For CUDA 12.1:
    ```
    pip install torch  --index-url https://download.pytorch.org/whl/cu121
    ```
    - For CUDA 12.4:
    ```
    pip install torch  --index-url https://download.pytorch.org/whl/cu124
    ```
- **For CPU (if not using GPU):**
  ```bash
  pip install torch
  ```
  This installs the CPU-only version of PyTorch.
