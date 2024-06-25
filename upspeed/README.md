# UpSpeed - File Upload and Management System

UpSpeed is a web application for uploading, managing, and downloading files. It provides an intuitive interface for users to upload single or multiple files, view uploaded files, and delete files if necessary.

## Features

- **File Upload:** Upload single or multiple files with ease.
- **File Management:** View, download, and delete uploaded files.
- **Pagination:** Navigate through uploaded files with pagination.
- **Secure Storage:** Files are securely stored and metadata is maintained for each upload.
- **Error Pages:** Customized error pages with a touch of humor for 404 and 405 errors.

## Prerequisites

- Python 3.6+
- Flask
- TQDM
- A MySQL database (or any supported database)

## Installation

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/upspeed.git
    cd upspeed
    ```

2. **Create a virtual environment and activate it:**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up the database:**
    - Ensure you have a MySQL database running.
    - Update the database configuration in `utils/db_config.py`.
    - Initialize the database:
        ```sh
        python app.py
        ```

5. **Run the application:**
    ```sh
    python app.py
    ```

6. **Visit the application:**
    Open your browser and go to `http://127.0.0.1:5000`.

## File Structure

- `app.py`: The main application file.
- `templates/`: HTML templates for the application.
- `static/css/`: CSS files for styling.
- `static/js/`: JavaScript files.
- `uploads/`: Directory where uploaded files are stored.
- `utils/db_config.py`: Database configuration and utility functions.
- `models/contact_models.py`: Models for managing contact form submissions.

## Usage

### Uploading Files
1. Navigate to the home page.
2. Click on "Upload Single" to upload a single file or "Upload Multiple" to upload multiple files.
3. Select the file(s) you want to upload and click "Upload".

### Viewing Uploaded Files
1. Click on the "Files" link in the navigation menu.
2. You will see a list of uploaded files along with their upload dates.

### Downloading Files
1. In the "Files" list, click on the "Download" link next to the file you want to download.
2. A dialog box will appear. Click "Yes" to confirm the download.

### Deleting Files
1. In the "Files" list, click on the "Delete" link next to the file you want to delete.
2. A dialog box will appear. Click "Yes" to confirm the deletion.

## Development

### Setting Up for Development
1. **Fork and clone the repository:**
    ```sh
    git clone https://github.com/harrunjibs/upspeed.git
    cd upspeed
    ```

2. **Install development dependencies:**
    ```sh
    pip install -r requirements-dev.txt
    ```

3. **Run the development server:**
    ```sh
    flask run
    ```

### Running Tests
1. **Run unit tests:**
    ```sh
    pytest
    ```

## Deployment

### Deploying to Heroku
1. **Create a new Heroku app:**
    ```sh
    heroku create your-app-name
    ```

2. **Set up Heroku environment variables:**
    ```sh
    heroku config:set SECRET_KEY=your_secret_key
    heroku config:set DATABASE_URL=your_database_url
    ```

3. **Deploy the application:**
    ```sh
    git push heroku main
    ```

4. **Open the app in your browser:**
    ```sh
    heroku open
    ```

## Custom Error Pages

- **404 Not Found:** If a page is not found, enjoy a humorous take on the situation!
- **405 Method Not Allowed:** When a method is not allowed, we'll lighten the mood with a witty message.

## Acknowledgements
- This project is built with [Flask](https://flask.palletsprojects.com/).
- Icons used in the application are from [FontAwesome](https://fontawesome.com/).

## Contact
For any inquiries, please contact us at [harzkane@gmail.com](mailto:harzkane@gmail.com).

## Contributing

Contributions are welcome! Please fork the repository and submit pull requests for any features or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
