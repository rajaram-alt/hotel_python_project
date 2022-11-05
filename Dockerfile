FROM python:3.9 
# Or any preferred Python version.
ADD hotel_project.py .
ADD error_log.txt .
ADD log.txt .
ADD hotel_project_testing.py .
CMD ["python","./hotel_project_testing.py"] 
# Or enter the name of your unique directory and parameter set.