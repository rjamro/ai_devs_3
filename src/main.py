import os
from domains import TaskPayload, TaskResponse
import requests
import importlib
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
ENDPOINT = os.getenv("ENDPOINT")


def get_task_answer(task_id: str):
    module = importlib.import_module(f'tasks.{task_id}')
    Task = getattr(module, 'Task')

    return Task.execute()


def main():
    task_id = input(f'Enter task id: ')

    answer = get_task_answer(task_id=task_id)

    payload = TaskPayload(
        task=task_id,
        apikey=API_KEY,
        answer=answer
    )

    response = requests.post(
        url=ENDPOINT,
        json=payload.model_dump(),
    )

    try:
        decoded_response = TaskResponse(**response.json())
    except Exception as e:
        print(e)
        return
    else:
        print(f'The response code was: {decoded_response.code} and message: {decoded_response.message}')

if __name__ == "__main__":
    main()
