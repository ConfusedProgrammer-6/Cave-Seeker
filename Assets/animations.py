from Player import spritesheet_process
class Animation:
    def __init__(self):
        pass

    def jumpAnim(self, file):
        my_spritesheet = spritesheet_process.Spritesheet_process(file)
        jumper = [my_spritesheet.parse_sprite('jump1'),
                  my_spritesheet.parse_sprite('jump2'),
                  my_spritesheet.parse_sprite('jump3'),
                  my_spritesheet.parse_sprite('jump4'),
                  my_spritesheet.parse_sprite('jump5'),
                  my_spritesheet.parse_sprite('jump6')]
        return jumper

    def runAnim(self, direction, file):
        if direction > 0:
            my_spritesheet = spritesheet_process.Spritesheet_process(file)
            runner = [my_spritesheet.parse_sprite('runner1'),
                      my_spritesheet.parse_sprite('runner2'),
                      my_spritesheet.parse_sprite('runner3'),
                      my_spritesheet.parse_sprite('runner4'),
                      my_spritesheet.parse_sprite('runner5'),
                      my_spritesheet.parse_sprite('runner6'),
                      my_spritesheet.parse_sprite('runner7'),
                      my_spritesheet.parse_sprite('runner8'),
                      my_spritesheet.parse_sprite('runner9'),
                      my_spritesheet.parse_sprite('runner10'), ]
            return runner

    def idleAnim(self, file):
        my_spritesheet = spritesheet_process.Spritesheet_process(file)
        idler = [my_spritesheet.parse_sprite('idle1'),
                 my_spritesheet.parse_sprite('idle2'),
                 my_spritesheet.parse_sprite('idle3'),
                 my_spritesheet.parse_sprite('idle4')]
        return idler
