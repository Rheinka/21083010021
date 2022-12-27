import random
import string

def home():
  while True:
    print("                                                                         ")
    print("|=======================================================================|")
    print("|                    SELAMAT DATANG DI RHEI GAMES                       |")
    print("|-----------------------------------------------------------------------|")
    print("|                 SILAHKAN PILIH GAME YANG ANDA SUKA                    |")
    print("|1. Tebak Angka                                                         |")
    print("|2. Hangman                                                             |")
    print("|3. Keluar                                                              |")
    print("|=======================================================================|")
    pilih = int(input("Masukkan angka pilihan game: "))
    print()
    if(pilih==1):
      tebak_angka()
    elif(pilih==2):
      hangman()
    else:
      keluar()
      break

def keluar():
    print("|=======================================================================|")
    print("|                     Terima Kasih Sudah Bermain!                       |")
    print("|                          SAMPAI JUMPA :)                              |")
    print("|=======================================================================|")

def tebak_angka():
  while True:
    print("|=======================================================================|")
    print("|             Halo, Anda sedang ada dalam game tebak angka!             |")
    print("|-----------------------------------------------------------------------|")
    print("| Berikut aturan permainan dalam tebak angka ini :                      |")
    print("| 1. Anda memiliki 5 kali kesempatan untuk menjawab sampai benar!       |")
    print("| 2. Angka yang kalian tebak ada pada range 1-10                        |")
    print("| 3. Perhatikan clue yang diberikan                                     |")
    print("|-----------------------------------------------------------------------|")
    batas_percobaan = 5
    angka_acak = random.randint(1, 10)
    print("|            Kami telah memilih angka, silahkan anda tebak!             |")
    print("|=======================================================================|")
    for percobaan in range(batas_percobaan):
        jawaban = int(input(f'\n[Percobaan {percobaan + 1}] Masukkan angka: '))
        if jawaban == angka_acak:
            print("|=======================================================================|")
            print("|            Selamat, angka yang anda tebak adalah benar!               |")
            print("|=======================================================================|")
            break
        else:
            print('Angka yang kalian tebak terlalu', 'kecil' if jawaban < angka_acak else 'besar')

    else:
        print(f"      \nYahh maaf, Anda melewati batas percobaan {batas_percobaan}x.   ") 
        print("|---------------------------------------------------------------------|")
        print("|                    Silahkan coba lagi nanti!                        |")
        print("|=====================================================================|")

    ulang = input("Apakah kamu ingin bermain lagi? (Ya/Tidak) : ")
    print("\n")
    if ulang == "Ya" :
      tebak_angka()
    elif ulang == "Tidak" :
      print("|=======================================================================|")
      print("|              TERIMA KASIH SUDAH BERMAIN. SAMPAI JUMPA :)              |")
      print("|=======================================================================|")
    else:
      home()
    return

def hangman():
    print("|=======================================================================|")
    print("|                        SELAMAT DATANG DI HANGMAN                      |")
    print("|=======================================================================|")

    wordDictionary = ["bunga", "rumah", "mendung", "matahari", "telegram", "baju", "celana", "pagi", "siang", "malam", "sepatu", "topi", "hai", "hallo"]

    ### Choose a random word
    randomWord = random.choice(wordDictionary)

    for x in randomWord:
      print("_", end=" ")

    def print_hangman(wrong):
      if(wrong == 0):
        print("\n+---+")
        print("    |")
        print("    |")
        print("    |")
        print("   ===")
      elif(wrong == 1): 
        print("\n+---+")
        print("O   |")
        print("    |")
        print("    |")
        print("   ===")
      elif(wrong == 2):
        print("\n+---+")
        print("O   |")
        print("|   |")
        print("    |")
        print("   ===")
      elif(wrong == 3):
        print("\n+---+")
        print(" O  |")
        print("/|  |")
        print("    |")
        print("   ===")
      elif(wrong == 4):
        print("\n+---+")
        print(" O  |")
        print("/|\ |")
        print("    |")
        print("   ===")
      elif(wrong == 5):
        print("\n+---+")
        print(" O  |")
        print("/|\ |")
        print("/   |")
        print("   ===")
      elif(wrong == 6):
        print("\n+---+")
        print(" O   |")
        print("/|\  |")
        print("/ \  |")
        print("    ===")

    def printWord(guessedLetters):
      counter=0
      rightLetters=0
      for char in randomWord:
        if(char in guessedLetters):
          print(randomWord[counter], end=" ")
          rightLetters+=1
        else:
          print(" ", end=" ")
        counter+=1
      return rightLetters

    def printLines():
      print("\r")
      for char in randomWord:
        print("\u203E", end=" ")

    length_of_word_to_guess = len(randomWord)
    amount_of_times_wrong = 0
    current_guess_index = 0
    current_letters_guessed = []
    current_letters_right = 0

    while(amount_of_times_wrong != 6 and current_letters_right != length_of_word_to_guess):
      print("\nLetters guessed so far: ")
      for letter in current_letters_guessed:
        print(letter, end=" ")
      ### Prompt user for input
      letterGuessed = input("\nGuess a letter: ")
      ### User is right
      if(randomWord[current_guess_index] == letterGuessed):
        print_hangman(amount_of_times_wrong)
        ### Print word
        current_guess_index+=1
        current_letters_guessed.append(letterGuessed)
        current_letters_right = printWord(current_letters_guessed)
        printLines()
      ### User was wrong af
      else:
        amount_of_times_wrong+=1
        current_letters_guessed.append(letterGuessed)
        ### Update the drawing
        print_hangman(amount_of_times_wrong)
        ### Print word
        current_letters_right = printWord(current_letters_guessed)
        printLines()

home()
   
