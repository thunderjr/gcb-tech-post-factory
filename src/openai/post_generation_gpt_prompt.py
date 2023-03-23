post_generation_gpt_prompt = [
  {
    "role": "system",
    "content": (
      # "You are ChatGPT, a large language model trained by OpenAI, based on the GPT-3 architecture. "
      "Your task is to generate social media posts for an Instagram page about technology topics. "
      "Each post should have a title and a mid length content text, where it should be informative and hooks the audience. Provide 2 versions of the post: one with a code example and one without."
      "Return the results as a JSON string containing an array of objects with the following structure, containing the post data in it: "
      "{ title: string; text: string; code: string | null; }"
    ),
  },
  {
    "role": "assistant",
    "content": (
"""[
  {
    "title": "Intro to Machine Learning",
    "text": "Learn the basics of machine learning and build your first model.",
    "code": "from sklearn.datasets import load_iris\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.tree import DecisionTreeClassifier\n\nX, y = load_iris(return_X_y=True)\nX_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)\nclf = DecisionTreeClassifier()\nclf.fit(X_train, y_train)\n"
  },
  {
    "title": "Machine Learning Without Code",
    "text": "Discover how to leverage no-code platforms for machine learning projects.",
    "code": null
  }
]"""
    ),
  }
]
