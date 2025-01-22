
# Certificate Generator

**Certificate Generator** is a project I created to simplify the process of generating certificates when I am in charge of organizing events. Additionally, I have implemented functionality to send these certificates via email using Gmail.

## Example Email and Certificate
![Certificate](https://raw.githubusercontent.com/maliqpotter/certificate-generator/master/screens/example-sertifikat.png)
![Email](https://raw.githubusercontent.com/maliqpotter/certificate-generator/master/screens/example-email.png)

## Requirement 

* Python >= `3.10.xx`

## Preparation

In the `templates` folder, ensure you have the following three files:
1. `MiriamLibre-SemiBold.ttf`
2. `nama-peserta.csv`
3. `sertifikat-peserta.png`

Ensure the file names match the criteria mentioned above to prevent errors. This project also includes sample CSV and certificate files that were used to test and run the project.

For the CSV file, ensure it contains two columns named `nama` and `email`. The code is designed to work with CSV files that use semicolons (`;`) as separators.

To create an email password, follow the instructions provided here: [Google Mail Support](https://support.google.com/mail/answer/185833?hl=en).  

After creating the password, store it in a secure location.  

**Note:** Once you have sent all the generated certificates to the recipients, be sure to **delete the password**. This password is intended for one-time use only to minimize security risks.

## Installation

* Install necessary modules

```bash
pip install -r requirements.txt
```
* Create the `output` folder where the generated certificate files will be stored.

```bash
mkdir output
```

## Generate Certificate

To generate certificates, run the command below. Once the command is executed, wait for the program to complete the process. The generated certificates can be found in the `output` folder.

```bash
python main.py
```

## Send Certificate via GMail

* If you want to customize the subject and body of the email, you can modify them in the send-mail.py file by updating the following function:
```python
# Function to send email
def send_email(to_email, recipient_name):
    subject = "Sertifikat Kehadiran"
    body = f"""\
Selamat, {recipient_name}!

Sertifikat Kehadiran di anda sudah tersedia. Anda dapat mendownload pada attachment.
Terima kasih, semoga bermanfaat.

Salam,
Pengurus Event."""
```

* Copy the `.env.example` file and rename it to `.env`, then configure it as follows:
```env
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=<change to your username email>
SMTP_PASSWORD="<change to your password from App Password>"
```
* To start sending emails, run the following command and wait until all emails have been sent to the recipients 
```bash
python send-email.py
```

## Bring your Own Templates
If you'd like to use your own certificate design and font, you can make adjustments in the `main.py` file.

* To change the font and adjust the font size to fit the certificate fields, modify the following code:
```python
# Font configuration
font_path = "templates/MiriamLibre-SemiBold.ttf"
font_size = 85
```
By default, the participant's name is centered in the certificate name field.
* To adjust the horizontal position of the participant's name on the certificate, modify this code. Use `+` to move the name to the right and `-` to move it to the left. Example:
```python
    # Horizontal position (centered by default)
    text_x = (image_width - text_width) / 2 + 10
```

* To adjust the vertical position of the participant's name on the certificate, modify this code. Use `+` to move the name up and `-` to move it down. Example:
```python
    # Vertical position (adjust as needed)
    text_y = 500 + 40
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)