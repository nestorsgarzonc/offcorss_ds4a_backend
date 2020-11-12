import sqlalchemy


def get_db():
    """ Function to conect to data base in postgres """
    # Parameters
    host = "team-cv.cfsx82z4jthl.us-east-2.rds.amazonaws.com"
    user = "ds4a_69"
    port = "5432"
    password = "DS4A!2020"
    database = "postgres"

    # Create the engine with the db credentials
    engine = sqlalchemy.create_engine(
        f'postgresql://{user}:{password}@{host}:{port}/{database}', max_overflow=20)
    return engine
