# csc-technical-course

1. **Clone the Repository**
   First, you need to clone the repository to your local machine. You can do this using the following command in your terminal:

   ```
   git clone https://github.com/gweldit/ai-4-cybersec-course.git
   ```

2. **Navigate to the Project Directory**
   Once the repository is cloned, navigate to the project directory using:

   ```
   cd csc-technical-course
   ```

3. **Install the Dependencies**
   The repository has `requirements.txt` file, it means there are some Python dependencies that you need to install. You can install these using pip:

   ```
   pip install -r requirements.txt
   ```

4. **Run the Project**
   Now, you can run the project. However, make sure you have specified a python virtual enviroment. Virtual Enviroment create a python version, in your project run.

   1. **Open your terminal** and navigate to the directory where you cloned the GitHub repository.

   2. **Install the virtual environment package** if you haven't already. You can do this by running the following command:
      ```bash
          pip install virtualenv
      ```
   3. **Create a virtual environment**. You can do this by running the following command:

   ```bash
   virtualenv myvenv
   ```

   Here, `myvenv` is the name of your virtual environment. Also, you can name it anything you like.

   5. **Activate the virtual environment**. The command to do this varies based on your operating system:

   - On **Windows**, run:

     ```bash
     myvenv\Scripts\activate
     ```

   - On **macOS/Linux**, run:

     ```bash
     source myvenv/bin/activate
     ```

5. Now your virtual environment is activated and you can **install the necessary packages** (This is if you skip step 3). If the cloned repository has a `requirements.txt` file, you can install all required packages using the following command:

```bash
pip install -r requirements.txt
```

6. Once you've installed all necessary packages, you can **run your Python code** within this virtual environment.

Remember to deactivate the virtual environment once you're done by simply running:

```bash
deactivate
```

or

```bash
source deactivate
```

This isolates your Python environment for this specific project and does not interfere with other projects. It's a good practice to use virtual environments for your Python projects.
