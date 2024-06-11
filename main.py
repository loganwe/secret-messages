from tkinter import messagebox, simpledialog, Tk

def is_even(number):
    return number % 2 == 0

def get_even_letters(message):
    even_letters = []
    for counter in range(0, len(message)):
        if is_even(counter):
            even_letters.append(message[counter])
    return even_letters

def get_odd_letters(message):
    odd_letters = []
    for counter in range(0, len(message)):
        if not is_even(counter):
            odd_letters.append(message[counter])
    return odd_letters

def swap_letters(message):
    letter_list = []
    if not is_even(len(message)):
        message = message + 'x'
    even_letters = get_even_letters(message)
    odd_letters = get_odd_letters(message)
    for counter in range(0, int(len(message)/2)):
        letter_list.append(odd_letters[counter])
        letter_list.append(even_letters[counter])
    new_message = ''.join(letter_list)
    return new_message

def get_task():
    task = simpledialog.askstring('Task', 'Do you want to encrypt or decrypt?').lower()
    return task

def get_message():
    message = simpledialog.askstring('Message', 'Enter the secret message: ')
    return message

def copy_to_clipboard(root, text):
    root.clipboard_clear()
    root.clipboard_append(text)
    root.update()  # now it stays on the clipboard after the window is closed

root = Tk()
root.withdraw()

while True:
    task = get_task()
    if task == 'encrypt' or 'en':
        message = get_message()
        encryp_message = swap_letters(message)
        copy_to_clipboard(root, encryp_message)
        messagebox.showinfo('Encrypted Message', 'Message to encrypt is: ' + encryp_message + '\n(The message has been copied to the clipboard.)')
    elif task == 'decrypt' or "de":
        message = get_message()
        decryp_message = swap_letters(message)
      
        messagebox.showinfo('Decrypted Message', 'Message to decrypt is: ' + decryp_message.rstrip('x'))
    else:
        break
