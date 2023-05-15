"""base model class for AirBnB models"""
import uuid
from datetime import datetime
import models


class BaseModel():
    """Base model class"""
    def __init__(self, *args, **kwargs):
        """Initialization of the basemodel class"""

        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

    def save(self):
        self.updated_at = datetime.today()
        #models.storage.save()

    def to_dict(self):
        """method for creating a dictionary for the class method"""
        data_dict  = self.__dict__.copy()
        data_dict['created_at'] = self.created_at.isoformat()
        data_dict['updated_at'] = self.updated_at.isoformat()
        data_dict['__class__'] = self.__class__.__name__

        return data_dict

    def __str__(self):
        """string representation of the class"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)


