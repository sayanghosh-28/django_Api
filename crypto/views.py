'''from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from celery.result import AsyncResult
import uuid
import json
import urllib.parse
from .tasks import scrape_coin_data

@api_view(['POST'])
def start_scraping(request):
    coins = request.data.get('coins', [])
    if not coins:
        return Response({'error': 'No coins provided'}, status=status.HTTP_400_BAD_REQUEST)

    job_id = str(uuid.uuid4())
    task_mappings = {}

    for coin in coins:
        task = scrape_coin_data.apply_async(args=[coin])
        task_mappings[coin] = task.id

    task_mappings_json = json.dumps(task_mappings)
    return Response({'job_id': job_id, 'task_ids': task_mappings_json}, status=status.HTTP_202_ACCEPTED)

@api_view(['GET'])
def scraping_status(request, job_id):
    task_ids_encoded = request.query_params.get('task_ids', None)
    if not task_ids_encoded:
        return Response({'error': 'No task_ids provided'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        task_ids_json = urllib.parse.unquote(task_ids_encoded)
        task_mappings = json.loads(task_ids_json)
    except (json.JSONDecodeError, TypeError):
        return Response({'error': 'Invalid task_ids format'}, status=status.HTTP_400_BAD_REQUEST)

    tasks_data = []

    for coin, task_id in task_mappings.items():
        result = AsyncResult(task_id)
        if result.ready():
            tasks_data.append({'coin': coin, 'output': result.result})
        else:
            tasks_data.append({'coin': coin, 'output': 'Task not completed yet'})

    return Response({'job_id': job_id, 'tasks': tasks_data}, status=status.HTTP_200_OK)'''
    
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from celery.result import AsyncResult
import uuid
import json
import urllib.parse
from .tasks import test_task

@api_view(['POST'])
def start_scraping(request):
    coins = request.data.get('coins', [])
    if not coins:
        return Response({'error': 'No coins provided'}, status=status.HTTP_400_BAD_REQUEST)

    job_id = str(uuid.uuid4())
    task_mappings = {}

    for coin in coins:
        task = test_task.apply_async(args=[coin])
        task_mappings[coin] = task.id

    task_mappings_json = json.dumps(task_mappings)
    return Response({'job_id': job_id, 'task_ids': task_mappings_json}, status=status.HTTP_202_ACCEPTED)

@api_view(['GET'])
def scraping_status(request, job_id):
    task_ids_encoded = request.query_params.get('task_ids', None)
    if not task_ids_encoded:
        return Response({'error': 'No task_ids provided'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        task_ids_json = urllib.parse.unquote(task_ids_encoded)
        task_mappings = json.loads(task_ids_json)
    except (json.JSONDecodeError, TypeError):
        return Response({'error': 'Invalid task_ids format'}, status=status.HTTP_400_BAD_REQUEST)

    tasks_data = []

    for coin, task_id in task_mappings.items():
        result = AsyncResult(task_id)
        if result.ready():
            tasks_data.append({'coin': coin, 'output': result.result})
        else:
            tasks_data.append({'coin': coin, 'output': 'Task not completed yet'})

    return Response({'job_id': job_id, 'tasks': tasks_data}, status=status.HTTP_200_OK)




