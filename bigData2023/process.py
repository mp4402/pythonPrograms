import boto3
from pyathena import connect

# perfil sso para el ambiente de ejecucion
region_name = "us-east-1"
perfil_env = "Usuario3"
session = boto3.Session(profile_name=perfil_env)


#definicion para borrar objetos en el prefix de S3
def deletePrefix(bucket, prefix):
    s3_resource = session.resource(
        's3'
    )
    bucket = s3_resource.Bucket(bucket)
    print(bucket)
    print("Prefix Bucket to delete: ", prefix)
    bucket.objects.filter(Prefix=(prefix)).delete()
    print("Prefix deleted")

#definicion para ejecutar query en athena
def executeQueryAthena(Query):
    cursor = connect(duration_seconds=3600,
                     output_location=s3_output_location,
                     profile_name=perfil_env,
                     s3_staging_dir=s3_output_location,
                     region_name=region_name).cursor()

    print("Query to execute: ", Query)

    cursor.execute(
        Query
    )
    print("Query executed")

#variables

s3_output_location = "s3://logs-bigdata-ufm-mariopisquiy/logs_athena/"
bucket_name_stage = "stage-bigdata-ufm-mpisquiy"
bucket_name_analytics = "analytics-bigdata-ufm-mariopisquiy"
prefix_to_delete_stage = "stage_covid/mes=202302/"
prefix_to_delete_analytics = "smy_top_vaccine/fecha=20230202/"

sqlQuery_stage = """INSERT INTO ufm.stage_covid
SELECT location,
total_cases,
new_cases,
total_deaths,
new_deaths,
people_fully_vaccinated, substr(cast(fecha as varchar),1,6)  mes, cast(fecha as varchar) fecha
FROM UFM.DATOS_COVID_RAW"""

sqlQuery_analytics = """INSERT INTO ufm.smy_top_vaccine
SELECT location, people_fully_vaccinated as people_fully_vaccinated, fecha
FROM UFM.STAGE_COVID where fecha = '20230202'
order by 2 desc limit 10;"""

#Ejecución
deletePrefix(bucket_name_stage, prefix_to_delete_stage)
executeQueryAthena(sqlQuery_stage)
deletePrefix(bucket_name_analytics, prefix_to_delete_analytics)
executeQueryAthena(sqlQuery_analytics)