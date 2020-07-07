from marshmallow import Schema, fields


class LayerSchema(Schema):
    class Meta:
        fields = ("id",
                  "label",
                  "url",
                  )
        ordered = True


class ImageSchema(Schema):
    class Meta:
        fields = ("id",
                  "label",
                  "description",
                  "url",
                  "level",
                  )
        ordered = True

class MapSchema(Schema):
    class Meta:
        fields = ("id",
                  "label",
                  "description",
                  )
        ordered = True


class ReferenceSchema(Schema):
    class Meta:
        fields = ("id",
                  "label",
                  "description",
                  )
        ordered = True
