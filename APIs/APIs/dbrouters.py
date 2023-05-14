
class observedRouter:
    """
    A router to control all database operations on models in the
    auth and contenttypes applications.
    """
    route_app_labels = {'auth', 'contenttypes','admin','sessions','observed'}

    def db_for_read(self, model, **hints):
        """
        Attempts to read auth and contenttypes models go to auth_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'observed_db'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write auth and contenttypes models go to auth_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'observed_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the auth or contenttypes apps is
        involved.
        """
        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth and contenttypes apps only appear in the
        'auth_db' database.
        """
        if app_label in self.route_app_labels:
            return db == 'observed_db'
        return None

class observedClimatologyRouter:
    """
    A router to control all database operations on models in the
    auth and contenttypes applications.
    """              
    route_app_labels = {'observedClimatology'}
    

    def db_for_read(self, model, **hints):
        """
        Attempts to read auth and contenttypes models go to auth_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'bdClimatology'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth and contenttypes apps only appear in the
        'auth_db' database.
        """
        if app_label in self.route_app_labels:
            return db == 'bdClimatology'
        return None



class forecastRouter:
    """
    A router to control all database operations on models in the
    auth and contenttypes applications.
    """
    route_app_labels = {'forecast'}

    def db_for_read(self, model, **hints):
        """
        Attempts to read auth and contenttypes models go to auth_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'weather_api'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth and contenttypes apps only appear in the
        'auth_db' database.
        """
        if app_label in self.route_app_labels:
            return db == 'weather_api'
        return None

class postgresRouter:
    """
    A router to control all database operations on models in the
    auth and contenttypes applications.
    """

    route_app_labels = {'climatology'}

    def db_for_read(self, model, **hints):
        """
        Attempts to read auth and contenttypes models go to auth_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'remoteGIS'
        return None


    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth and contenttypes apps only appear in the
        'auth_db' database.
        """
        if app_label in self.route_app_labels:
            return db == 'remoteGIS'
        return None



class transportRouter:
    """
    A router to control all database operations on models in the
    auth and contenttypes applications.
    """
    route_app_labels = {'transport'}

    def db_for_read(self, model, **hints):
        """
        Attempts to read auth and contenttypes models go to auth_db.
        """
        if model._meta.app_label in self.route_app_labels:
            return 'transport'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the auth and contenttypes apps only appear in the
        'auth_db' database.
        """
        if app_label in self.route_app_labels:
            return db == 'transport'
        return None


