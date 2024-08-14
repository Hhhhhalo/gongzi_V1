from datetime import datetime


class NeituiService:
    @staticmethod
    def add_record(data):
        record = Neitui(**data)
        if 'create_time' not in data:
            record.create_time = datetime.utcnow()
        db.session.add(record)
        db.session.commit()
        return record

    @staticmethod
    def get_all_records():
        return Neitui.query.all()

    @staticmethod
    def get_record_by_id(record_id):
        return Neitui.query.get(record_id)

    @staticmethod
    def update_record(record_id, updates):
        record = Neitui.query.get(record_id)
        if record:
            for key, value in updates.items():
                setattr(record, key, value)
            db.session.commit()
            return record
        return None

    @staticmethod
    def delete_record(record_id):
        record = Neitui.query.get(record_id)
        if record:
            db.session.delete(record)
            db.session.commit()
            return True
        return False


class ShebaoService:
    @staticmethod
    def add_record(data):
        record = Shebao(**data)
        if 'create_time' not in data:
            record.create_time = datetime.utcnow()
        db.session.add(record)
        db.session.commit()
        return record

    @staticmethod
    def get_all_records():
        return Shebao.query.all()

    @staticmethod
    def get_record_by_id(record_id):
        return Shebao.query.get(record_id)

    @staticmethod
    def update_record(record_id, updates):
        record = Shebao.query.get(record_id)
        if record:
            for key, value in updates.items():
                setattr(record, key, value)
            db.session.commit()
            return record
        return None

    @staticmethod
    def delete_record(record_id):
        record = Shebao.query.get(record_id)
        if record:
            db.session.delete(record)
            db.session.commit()
            return True
        return False


class YibaoService:
    @staticmethod
    def add_record(data):
        record = Yibao(**data)
        if 'create_time' not in data:
            record.create_time = datetime.utcnow()
        db.session.add(record)
        db.session.commit()
        return record

    @staticmethod
    def get_all_records():
        return Yibao.query.all()

    @staticmethod
    def get_record_by_id(record_id):
        return Yibao.query.get(record_id)

    @staticmethod
    def update_record(record_id, updates):
        record = Yibao.query.get(record_id)
        if record:
            for key, value in updates.items():
                setattr(record, key, value)
            db.session.commit()
            return record
        return None

    @staticmethod
    def delete_record(record_id):
        record = Yibao.query.get(record_id)
        if record:
            db.session.delete(record)
            db.session.commit()
            return True
        return False