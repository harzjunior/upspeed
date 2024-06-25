from flask import Flask, request, render_template, redirect, send_from_directory, url_for, flash # type: ignore
import os
import sys
import json
import time
import uuid
from werkzeug.utils import secure_filename # type: ignore
from tqdm import tqdm # type: ignore
from math import ceil

# Add the project root directory to the sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from upspeed.utils.db_config import get_db  # Importing the database connection function # type: ignore

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for flash messages
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
FILES_PER_PAGE = 10

# Ensure uploads folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Function to initialize database (if needed)
def init_db():
    with get_db() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY AUTO_INCREMENT,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                message TEXT NOT NULL
            );
        """)
        conn.commit()

# Initialize database on application startup
init_db()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/file_list')
def file_list():
    page = request.args.get('page', 1, type=int)
    all_files = os.listdir(app.config['UPLOAD_FOLDER'])
    
    # Filter out metadata files
    actual_files = [file for file in all_files if not file.endswith('.json')]
    
    total_files = len(actual_files)
    total_pages = ceil(total_files / FILES_PER_PAGE)
    
    start = (page - 1) * FILES_PER_PAGE
    end = start + FILES_PER_PAGE
    
    files_on_page = actual_files[start:end]
    
    file_infos = []
    for file in files_on_page:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file)
        metadata_path = file_path + '.json'
        if os.path.exists(metadata_path):
            with open(metadata_path, 'r') as metadata_file:
                metadata = json.load(metadata_file)
            file_infos.append({
                'name': file,
                'date': metadata['upload_date']
            })
    
    return render_template('file_list.html', files=file_infos, page=page, total_pages=total_pages, max=max, min=min)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        # Insert into MySQL database
        try:
            with get_db() as conn:
                cursor = conn.cursor()
                sql = "INSERT INTO contacts (name, email, message) VALUES (%s, %s, %s)"
                cursor.execute(sql, (name, email, message))
                conn.commit()
                flash('Message submitted successfully!', 'success')  # Flash success message
        except Exception as e:
            flash(f'Error: {str(e)}', 'error')  # Flash error message
        finally:
            return redirect('/contact')
    
    return render_template('contact.html')

@app.route('/upload_single')
def upload_single():
    return render_template('upload_single.html', origin='single')

@app.route('/upload_file', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        flash('No file part', 'error')
        return redirect(request.url)
    
    file = request.files['file']
    if file.filename == '':
        flash('No selected file', 'error')
        return redirect(request.url)
    
    original_filename = secure_filename(file.filename)
    file_ext = os.path.splitext(original_filename)[1]
    unique_filename = f"{uuid.uuid4().hex}{file_ext}"
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
    
    start_time = time.time()
    total_size = 0
    chunk_size = 4096
    progress_bar = tqdm(total=int(request.content_length), unit='B', unit_scale=True)

    try:
        with open(file_path, 'wb') as f:
            while True:
                chunk = file.stream.read(chunk_size)
                if not chunk:
                    break
                f.write(chunk)
                total_size += len(chunk)
                progress_bar.update(len(chunk))
    except Exception as e:
        flash(f'Error uploading file: {str(e)}', 'error')
        return redirect(request.url)
    finally:
        progress_bar.close()

    end_time = time.time()
    upload_time = end_time - start_time
    upload_speed = total_size / upload_time

    # Save metadata
    metadata = {
        'original_filename': original_filename,
        'upload_date': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    }
    metadata_path = file_path + '.json'
    with open(metadata_path, 'w') as metadata_file:
        json.dump(metadata, metadata_file)

    flash('File uploaded successfully!', 'success')
    return redirect(url_for('upload_result', origin='single', 
                            message='File uploaded successfully',
                            size=f"{total_size / (1024 * 1024):.2f} MB",
                            time=f"{upload_time:.2f} seconds",
                            speed=f"{upload_speed / 1024:.2f} KB/s"))

@app.route('/upload_multiple')
def upload_multiple():
    return render_template('upload_multiple.html', origin='multiple')

@app.route('/upload_multiple_files', methods=['POST'])
def upload_multiple_files():
    if 'files' not in request.files:
        flash('No file part', 'error')
        return redirect(request.url)
    
    files = request.files.getlist('files')
    responses = []

    for file in files:
        if file.filename == '':
            flash('No selected file', 'error')
            return redirect(request.url)
        
        original_filename = secure_filename(file.filename)
        file_ext = os.path.splitext(original_filename)[1]
        unique_filename = f"{uuid.uuid4().hex}{file_ext}"
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
        
        start_time = time.time()
        total_size = 0
        chunk_size = 4096
        progress_bar = tqdm(total=int(request.content_length), unit='B', unit_scale=True)

        try:
            with open(file_path, 'wb') as f:
                while True:
                    chunk = file.stream.read(chunk_size)
                    if not chunk:
                        break
                    f.write(chunk)
                    total_size += len(chunk)
                    progress_bar.update(len(chunk))
        except Exception as e:
            flash(f'Error uploading file: {str(e)}', 'error')
            return redirect(request.url)
        finally:
            progress_bar.close()

        end_time = time.time()
        upload_time = end_time - start_time
        upload_speed = total_size / upload_time

        # Save metadata
        metadata = {
            'original_filename': original_filename,
            'upload_date': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        }
        metadata_path = file_path + '.json'
        with open(metadata_path, 'w') as metadata_file:
            json.dump(metadata, metadata_file)

        response = {
            'message': f'File "{original_filename}" uploaded successfully',
            'size': f"{total_size / (1024 * 1024):.2f} MB",
            'time': f"{upload_time:.2f} seconds",
            'speed': f"{upload_speed / 1024:.2f} KB/s"
        }
        responses.append(response)

    flash('Files uploaded successfully!', 'success')
    return redirect(url_for('upload_result', origin='multiple',
                            message='Files uploaded successfully',
                            size=f"{total_size / (1024 * 1024):.2f} MB",
                            time=f"{upload_time:.2f} seconds",
                            speed=f"{upload_speed / 1024:.2f} KB/s",
                            count=len(responses)))

@app.route('/upload_result')
def upload_result():
    origin = request.args.get('origin', '')
    if origin == 'single':
        return render_template('upload_result.html', single_result=request.args)
    elif origin == 'multiple':
        return render_template('upload_result.html', multiple_result=request.args)
    else:
        return redirect(url_for('index'))

@app.route('/uploads/<filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/delete/<filename>')
def delete_file(filename):
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if os.path.exists(file_path):
        os.remove(file_path)
        flash(f'File "{filename}" has been deleted successfully.', 'success')
        return redirect('/file_list')

if __name__ == '__main__':
    app.run(debug=True)