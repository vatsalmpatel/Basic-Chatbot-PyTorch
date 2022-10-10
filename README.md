# Basic Chatbot with PyTorch

Here, I have built a basic chatbot 💻 for an e-commerce website that sells tea 🍵 and coffee ☕. This chatbot has very basic functionalities such as greetings, chat is the website selling, the payments methods 🏧 and much more.

This is based on a simple feed-forward neural network trained on a small dataset. The data file is in json format so ,if you want to look at the data on which the chatbot has trained on refer to `data.json` file.

# A brief introduction to all the files 🗃

⏩ `model.py` ➡ The feed-forward neural network to train the data and create the model for conversation.

⏩ `chat.py` ➡ File where all the pieces of the chatbot system comes together. It imports the trained model and loads it to hold a chat with another person 🧔. It launches a chat application in the terminal itself and the chat goes on until the user of the application types `quit`❌.

⏩ `data.pth` ➡ The model file where the trained model is stored from PyTorch. It contains all the necessary information such as the input size to the model, the words on which the model is trained on, the model parameters after the model has been trained on the training data.

⏩ `train.py` ➡ The training file for the chatbot. This fild houses the Neural Network for training as well creating dataset out of the `data.json` file as well as the training loop for training the model.

⏩ `utils.py` ➡ This file has all the necessary nltk functions implemented for stemming and tokenizing the data as well creating bad of words from the sentences.

# ❓ How to use the Chatbot ❓

Well, that's a great question. If you are using anaconda, you just need to create a new environment using:

```Bash
conda create -n new_env_name
```

Do not forget to activate you new environment:

```Bash
conda activate new_env_name
```

After you have created the new environment, just install all the dependencies with the `requirements.txt` file already bundeled with this repo using:

```Bash
pip install -r requirements.txt
```

Just one last step, launch the chatbot application by ivoking the `chat.py` file:

```Bash
python chat.py
```

# Work Samples 🧪

![Work Sample](images/sample_work.jpg)

### And there you have it ✅, you have successfully created a chatbot using nltk and PyTorch. ⚠ This is just avery basic chatbot, you can build upon this framework and create chatbots specific to your application and usecase. 🏁