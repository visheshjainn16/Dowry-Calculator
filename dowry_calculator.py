{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "vHSkUz3HqQDL",
        "outputId": "b8135aac-a8f2-4133-db1d-1ee41d1821e1"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "💍 Welcome to the Fun Dowry Calculator 💰 (Parody Project)\n",
            "-----------------------------------------------------------\n",
            "Enter your name: Vishesh\n",
            "Enter your age: 19\n",
            "Your highest degree (BTech / MTech / PhD / Dropout): BTech\n",
            "College tier (Tier 1 / Tier 2 / Tier 3 / Local): Tier 3\n",
            "Job role (None / Software Dev / AI Engineer / Govt Officer): AI engineer\n",
            "Annual Salary in Lakhs ₹: 2000000\n",
            "Your height in cm (Just for fun): 180\n",
            "Special skills (Cooks / Codes / Sings / None): cooks\n",
            "Self-rated looks (1 to 10): 7\n",
            "\n",
            "Thanks! Calculating your ideal fun dowry demand... 😂\n"
          ]
        }
      ],
      "source": [
        "# 🧠 Dowry Calculator - Just for Fun 😄\n",
        "print(\"💍 Welcome to the Fun Dowry Calculator 💰 (Parody Project)\")\n",
        "print(\"-----------------------------------------------------------\")\n",
        "\n",
        "# Taking user inputs\n",
        "name = input(\"Enter your name: \")\n",
        "age = int(input(\"Enter your age: \"))\n",
        "degree = input(\"Your highest degree (BTech / MTech / PhD / Dropout): \")\n",
        "college = input(\"College tier (Tier 1 / Tier 2 / Tier 3 / Local): \")\n",
        "job = input(\"Job role (None / Software Dev / AI Engineer / Govt Officer): \")\n",
        "salary = int(input(\"Annual Salary in Lakhs ₹: \"))\n",
        "height = int(input(\"Your height in cm (Just for fun): \"))\n",
        "skills = input(\"Special skills (Cooks / Codes / Sings / None): \")\n",
        "looks = int(input(\"Self-rated looks (1 to 10): \"))\n",
        "\n",
        "print(\"\\nThanks! Calculating your ideal fun dowry demand... 😂\")\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# 💰 Start with a base dowry value\n",
        "dowry = 5  # in Lakhs\n",
        "\n",
        "# 🎓 Degree bonus\n",
        "if degree == \"PhD\":\n",
        "    dowry += 20\n",
        "elif degree == \"MTech\":\n",
        "    dowry += 15\n",
        "elif degree == \"BTech\":\n",
        "    dowry += 10\n",
        "elif degree == \"Dropout\":\n",
        "    dowry -= 5\n",
        "\n",
        "# 🏫 College tier bonus\n",
        "if college == \"Tier 1\":\n",
        "    dowry += 10\n",
        "elif college == \"Tier 2\":\n",
        "    dowry += 5\n",
        "elif college == \"Tier 3\":\n",
        "    dowry += 2\n",
        "else:\n",
        "    dowry -= 2\n",
        "\n",
        "# 💼 Job bonus\n",
        "if job == \"AI Engineer\":\n",
        "    dowry += 15\n",
        "elif job == \"Software Dev\":\n",
        "    dowry += 10\n",
        "elif job == \"Govt Officer\":\n",
        "    dowry += 20\n",
        "elif job == \"None\":\n",
        "    dowry -= 5\n",
        "\n",
        "# 💸 Salary bonus\n",
        "dowry += salary * 0.8  # 80% of salary added as bonus\n",
        "\n",
        "# 📏 Height bonus (just for laughs 😄)\n",
        "if height > 180:\n",
        "    dowry += 5\n",
        "elif height < 160:\n",
        "    dowry -= 2\n",
        "\n",
        "# 🛠 Skills bonus\n",
        "if \"Cooks\" in skills:\n",
        "    dowry += 5\n",
        "if \"Codes\" in skills:\n",
        "    dowry += 5\n",
        "if \"Sings\" in skills:\n",
        "    dowry += 3\n",
        "\n",
        "# 😎 Looks bonus\n",
        "dowry += looks * 1.5\n",
        "\n",
        "# 🧮 Final result\n",
        "dowry = round(dowry, 2)\n"
      ],
      "metadata": {
        "id": "VqoBPG3YrBAb"
      },
      "execution_count": 5,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# 🎉 Display the final funny output\n",
        "print(\"-----------------------------------------------------------\")\n",
        "print(f\"🎩 Hello {name}, based on your elite profile 🤓...\")\n",
        "print(f\"💰 Your ideal *dowry demand* is: ₹{dowry} Lakhs! 💸\")\n",
        "\n",
        "# Funny bonus comments\n",
        "if dowry > 60:\n",
        "    print(\"🏆 You're premium! Time to ask for gold-plated horses too.\")\n",
        "elif dowry > 40:\n",
        "    print(\"🔥 Solid profile! Aunties will be fighting over you.\")\n",
        "elif dowry > 20:\n",
        "    print(\"😎 Respectable! But work on your cooking skills maybe?\")\n",
        "else:\n",
        "    print(\"🤣 Hmm... maybe you should give dowry instead. Just kidding!\")\n",
        "\n",
        "# 📢 Disclaimers\n",
        "print(\"\\n⚠️ Disclaimer: This project is purely for fun and educational purposes.\")\n",
        "print(\"🚫 Say NO to dowry in real life. Support equality and love 💛\")\n",
        "print(\"-----------------------------------------------------------\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Yq2lR1Gfrd5p",
        "outputId": "acb415d3-2e0f-4a1c-8d5f-f407f15ae5d6"
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "-----------------------------------------------------------\n",
            "🎩 Hello Vishesh, based on your elite profile 🤓...\n",
            "💰 Your ideal *dowry demand* is: ₹1600027.5 Lakhs! 💸\n",
            "🏆 You're premium! Time to ask for gold-plated horses too.\n",
            "\n",
            "⚠️ Disclaimer: This project is purely for fun and educational purposes.\n",
            "🚫 Say NO to dowry in real life. Support equality and love 💛\n",
            "-----------------------------------------------------------\n"
          ]
        }
      ]
    }
  ]
}
