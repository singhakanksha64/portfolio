from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)

#@app.route('/<username>/<int:user_id>')
# def hello_world(username=None, user_id=None):
#
#     return render_template('index.html', name=username, uid=user_id)
@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/<string:page_name>')
def pagename(page_name):
    return render_template(page_name)


def write_to_dbfile(data):
    with open('database.txt', 'a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', 'a') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writes = csv.writer(database2, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writes.writerow([email,subject,message])





@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method =='POST':
        try:
            data = request.form.to_dict()
            #print(data)
            write_to_dbfile(data)
            write_to_csv(data)
            return redirect('thankyou.html')
        except:
            print('Bad query called')
    else:
        return "Something went wrong!"
    return 'Form submitted successfully'
