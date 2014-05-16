from ferris import BasicModel
from google.appengine.ext import ndb
from google.appengine.api import users


class Trainer(BasicModel):
    email = ndb.StringProperty(required=True)
    firstName = ndb.StringProperty(required=True)
    lastName = ndb.StringProperty(required=True)
    schoolDistrict = ndb.StringProperty()
    schoolName = ndb.StringProperty(required=True)
    schoolAddress1 = ndb.StringProperty()
    schoolAddress2 = ndb.StringProperty()
    schoolAddressCity = ndb.StringProperty()
    schoolAddressState = ndb.StringProperty()
    schoolAddressZip = ndb.StringProperty()
    bio = ndb.TextProperty()

    @classmethod
    def all_trainers(cls):
        """
        Queries all trainer in the system, ordered by date created descending.
        """
        return cls.query().order(-cls.created)

