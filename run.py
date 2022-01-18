"""
Execute the programme
"""
import json
from sqlite3 import OperationalError
from app import config, BASE
from pathlib import Path
from app.services.query import Query
from sqlalchemy.exc import IntegrityError

# FILE PATH
file = Path(BASE).joinpath(config['DATAFILE']['FILENAME'])


def run_app():
    try:
        data_file = open(file, 'r+')
        for data in data_file.readlines():
            json_data = json.loads(data)
            if json_data.get('source_table') == "Employee":
                Query.employee(json_data)
            elif json_data.get('source_table') == "Job":
                Query.job(json_data)
            elif json_data.get('source_table') == "Position":
                Query.position(json_data)
    except FileNotFoundError as f:        
        print(f"Exception occured: {f}")
    except IntegrityError as e:
        print(f"Duplicate data: {e}")
    except OperationalError as e:
        print(f"Operation Error: {e}")
    except Exception as e:
        print(f"Exception: {e}")


if __name__ == '__main__':
    run_app()
