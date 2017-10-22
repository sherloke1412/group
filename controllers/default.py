def index():
    record = db(db.images.id == 3).select()
    if len(record):
        record = record[0]
    return dict(message=T('Group Grading'),record=record)

def user():
    if request.args(0) == 'profile':
        db.auth_user.username.writable = False
        db.auth_user.username.readable = False
        db.auth_user.profile_picture.writable = True
    return dict(form=auth())

@cache.action()
def download():
    return response.download(request, db)


def call():
    return service()

def blank():
    return dict(message=T('Blank Page'))
