# Orbi Windows Client

This is the Windows client for the Orbi API. You need a running Orbi API server to use this.

> [!WARNING]
> Orbi Client ("the software") is provided "as is" without warranties of any kind. We are not liable for any damages arising from its use, including the capture or misuse of screenshots containing sensitive information. The software may capture passwords, DRM-protected content, and copyrighted material.
>
> By using Orbi Client, you agree to comply with all applicable laws. Your use of the software is at your own risk. We do not warrant it will be error-free or free from harmful components.
>
> We are not affiliated with Microsoft. Orbi Client is licensed under GPLv3. By downloading, installing, or using the software, you acknowledge that you have read, understood, and agree to this disclaimer.

## Setup

1. Create a new virtual environment:
    ```sh
    python -m venv .venv
    ```

2. Activate the virtual environment:
    ```sh
    .venv\Scripts\activate
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Run the main script:
    ```sh
    python main.py
    ```

## License

This project is licensed under the [GPLv3.0 License](LICENSE).