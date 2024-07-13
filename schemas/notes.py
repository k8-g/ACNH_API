from init import ma

class NotesSchema(ma.Schema):
    class Meta:
        fields = ("notes_id", "wanted_id", "villager_id", "notes")

# to handle a single note object
note_schema = NotesSchema()

# to handle a list of note objects
notes_schema = NotesSchema(many=True)