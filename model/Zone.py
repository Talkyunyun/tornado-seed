# coding=utf-8


from model.BaseModel import BaseModel


class Zone(BaseModel):

    def __init__(self):
        super(Zone, self).__init__(table='t_zone')
