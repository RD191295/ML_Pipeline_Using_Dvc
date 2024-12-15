import os

print("Data Ingestion Started")
os.system("python src/data_ingestion.py")
print("Data Ingestion complete")

print("Data preprocessing started")
os.system("python src/data_preprocessing.py")
print("Data preprocessing completed")

print("Feature Engineering started")
os.system("python src/feature_engineering.py")
print("Feature Engineering completed")

print("trainging model started")
os.system("python src/model_building.py")
print("trainging model completed")

print("evalution of model started")
os.system("python src/model_evalution.py")
print("evalution of model completed")