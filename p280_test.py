from flask import Flask, render_template,url_for, request, redirect
import os, csv
os.system('clear')

#a riable set up for directory of database.txt file 
app = Flask(__name__)  # Initialize Flask app
print(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')  
def html_page(page_name):
    return render_template(f"{page_name}.html")  # Ensure .html extension

#writing data to a file
def write_to_file(data):
	# Open Database.txt and write to it
    with open('database.txt', mode='a', newline='') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email},{subject},{message}')

#writing data to a csv file       
def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message]) 

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_file(data)
            write_to_csv(data) 
            return redirect('/thankyou')
        except:
            return 'Did not save to database' 
    else:
        return 'Something went wrong. Try again!'
        

if __name__ == '__main__':
    app.run(debug=True)