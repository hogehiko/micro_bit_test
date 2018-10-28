import music
import microbit


class Display:
    def set_seed_hash(self, hash):
        pass

    def set_step(self, step):
        pass

    def update(self):
        pass

class Sequence:
    def get_note(self):
        pass

class Seed:
    def update_sensors(self):
        pass

    def get_hash(self):
        pass

    def update(self):
        pass


display = Display()
sequence = Sequence()
seed = Seed()

freezeSeed = False
STEPS = 16
step = 0
bpm = 120 
interval = 60 * 1000 / bpm

while True:
    if not freezeSeed:
        seed.update_sensors()
    note = sequence.get_note()
    # TODO ouptput sound

    display.set_seed_hash(seed.get_hash())
    display.set_step(step)
    display.update()
    
    microbit.sleep(interval)
    
