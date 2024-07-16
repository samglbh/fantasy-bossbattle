@namespace
class SpriteKind:
    healthBar = SpriteKind.create()
    magicBar = SpriteKind.create()
    slot1 = SpriteKind.create()
    slot2 = SpriteKind.create()
    slot3 = SpriteKind.create()
    spell = SpriteKind.create()

def on_left_pressed():
    mySprite.image.flip_x()
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_right_pressed():
    mySprite.image.flip_x()
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

mySprite9: Sprite = None
mySprite8: Sprite = None
mySprite7: Sprite = None
mySprite6: Sprite = None
mySprite5: Sprite = None
mySprite4: Sprite = None
statusbar: StatusBarSprite = None
mySprite3: Sprite = None
mySprite: Sprite = None
name = game.ask_for_string("name", 12)
story.print_dialog("choose a class", 80, 100, 50, 150)
story.show_player_choices("mage", "warrior")
story.print_dialog("choose a subclass", 80, 100, 50, 150)
if story.check_last_answer("warrior"):
    story.show_player_choices("barbarian", "ranger", "rogue")
    if story.check_last_answer("barbarian"):
        mySprite = sprites.create(img("""
                . . . . . . d d d d . . . . . . 
                            . . . . . 4 d d d d 4 . . . . . 
                            . . . . . d 4 4 4 4 d . . . . . 
                            . . . e e 4 d d d d 4 e e . . . 
                            . . e e e 4 d d d d 4 e e e . . 
                            . . . d e e 4 d d 4 e e d . . . 
                            . . . d e e e e e e e e d . . . 
                            . . d d e e e e e e e e d d . . 
                            . . d d e e e e e e e e d d . . 
                            . d d d e e e e e e e e d d d . 
                            . d d d e e e 5 5 e e e d d d . 
                            . d d d . 2 2 2 2 2 2 . d d d . 
                            . d d d . e e e e e e . d d d . 
                            . d d d d f f f f f f d d d d . 
                            . d d d . d d . . d d . d d d . 
                            . . . . . d d . . d d . . . . . 
                            . . . . d d d . . d d d . . . .
            """),
            SpriteKind.player)
    elif story.check_last_answer("ranger"):
        mySprite = sprites.create(img("""
                ....ff..........
                            ....fefff.......
                            ...feeeeeff.....
                            ..feeeeeeeef....
                            .feeeeeeeeeef...
                            .feeeeeeebeeef..
                            feeebbbbbdbeef..
                            feebdddddddbeef.
                            .fbdddddddddbf..
                            .fdddfdddfddf...
                            ..fddfdddfddf...
                            ...fdddddddf....
                            ...f666666bf....
                            ..fbb6666bbbf...
                            ..fbbbbbbbbbf...
                            .fbbbc666cbbbf..
                            .fdbcc666ccbdf..
                            .fddc6666ccddf..
                            ..fbc6cc66cbf...
                            ..fbccbbcccbf...
                            ..fcfbcbbbfcf...
                            ...ffeefeeff....
                            .....ff.ff......
            """),
            SpriteKind.player)
    else:
        mySprite = sprites.create(img("""
                ....ff..........
                            ....fefff.......
                            ...feeeeeff.....
                            ..feeeeeeeef....
                            .feeeeeeeeeef...
                            .feeeeeeebeeef..
                            feeebbbbbdbeef..
                            feebdddddddbeef.
                            .fbdddddddddbf..
                            .fdddfdddfddf...
                            ..fddfdddfddf...
                            ...fdddddddf....
                            ...f666666cf....
                            ..fcc6666cccf...
                            ..fcccccccccf...
                            .fcccb444bcccf..
                            .fdcbb444bbcdf..
                            .fddb4444bbddf..
                            ..fcb4bb44bcf...
                            ..fcbbccbbbcf...
                            ..fbfcbcccfbf...
                            ...ffeefeeff....
                            .....ff.ff......
            """),
            SpriteKind.player)
else:
    mySprite3 = sprites.create(img("""
            . . . 4 4 4 . . . 
                    . . b b b b b . . 
                    . . b 4 4 4 b . . 
                    . . . b . b . . . 
                    . . . b . b . . . 
                    . . b . . . b . . 
                    . b 6 b 6 6 6 b . 
                    b 6 b 6 6 6 6 6 b 
                    b 6 b 6 6 6 b 6 b 
                    b 6 6 6 6 6 b 6 b 
                    b b 6 6 6 b 6 b b 
                    . . b b b b b . .
        """),
        SpriteKind.magicBar)
    mySprite3.set_position(105, 15)
    statusbar = statusbars.create(20, 4, StatusBarKind.magic)
    statusbar.set_position(120, 15)
    statusbar.set_bar_size(100, 4)
    statusbar.set_color(6, 12)
    mySprite4 = sprites.create(img("""
            . . . c d d d d d d d d c . . . 
                    . . c d b b b b b b b b d c . . 
                    . c d b b b b b b b b b b d c . 
                    c d b b b b b b b b b b b b d c 
                    d b b b b b b b b b b b b b b d 
                    d b b b b b b b b b b b b b b d 
                    d b b b b b b b b b b b b b b d 
                    d b b b b b b b b b b b b b b d 
                    d b b b b b b b b b b b b b b d 
                    d b b b b b b b b b b b b b b d 
                    d b b b b b b b b b b b b b b d 
                    d b b b b b b b b b b b b b b d 
                    c d b b b b b b b b b b b b d c 
                    . c d b b b b b b b b b b d c . 
                    . . c d b b b b b b b b d c . . 
                    . . . c d d d d d d d d c . . .
        """),
        SpriteKind.slot1)
    mySprite5 = sprites.create(img("""
            . . . c d d d d d d d d c . . . 
                    . . c d b b b b b b b b d c . . 
                    . c d b b b b b b b b b b d c . 
                    c d b b b b b b b b b b b b d c 
                    d b b b b b b b b b b b b b b d 
                    d b b b b b b b b b b b b b b d 
                    d b b b b b b b b b b b b b b d 
                    d b b b b b b b b b b b b b b d 
                    d b b b b b b b b b b b b b b d 
                    d b b b b b b b b b b b b b b d 
                    d b b b b b b b b b b b b b b d 
                    d b b b b b b b b b b b b b b d 
                    c d b b b b b b b b b b b b d c 
                    . c d b b b b b b b b b b d c . 
                    . . c d b b b b b b b b d c . . 
                    . . . c d d d d d d d d c . . .
        """),
        SpriteKind.slot2)
    mySprite6 = sprites.create(img("""
            . . . c d d d d d d d d c . . . 
                    . . c d b b b b b b b b d c . . 
                    . c d b b b b b b b b b b d c . 
                    c d b b b b b b b b b b b b d c 
                    d b b b b b b b b b b b b b b d 
                    d b b b b b b b b b b b b b b d 
                    d b b b b b b b b b b b b b b d 
                    d b b b b b b b b b b b b b b d 
                    d b b b b b b b b b b b b b b d 
                    d b b b b b b b b b b b b b b d 
                    d b b b b b b b b b b b b b b d 
                    d b b b b b b b b b b b b b b d 
                    c d b b b b b b b b b b b b d c 
                    . c d b b b b b b b b b b d c . 
                    . . c d b b b b b b b b d c . . 
                    . . . c d d d d d d d d c . . .
        """),
        SpriteKind.slot3)
    mySprite4.set_position(50, 15)
    mySprite5.set_position(30, 15)
    mySprite6.set_position(70, 15)
    story.show_player_choices("warlock", "wizard", "cleric")
    if story.check_last_answer("warlock"):
        mySprite = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . f f f f f . . . . . . . . . 
                            . f a a a a a f . . . . . . . . 
                            f a f f a a a a f . . . . . . . 
                            a f f a a a a a f . . . . . . . 
                            a f b a a a a a a f . . . . . . 
                            f b b d d f d f d 8 f . . . . . 
                            . f b b d d d d b f . . . . . . 
                            . f b b b b b b b f . . . . . . 
                            . . f b b b d b f . . . . . . . 
                            . . f a b b b b f . . . . . . . 
                            . f . f a b b a f f f . . . . . 
                            . f . . f b b a 4 4 f . . . . . 
                            . f f f a a b a f f . . . . . . 
                            f a a a a a b a a f . . . . . . 
                            f f f f f f f f f f . . . . . .
            """),
            SpriteKind.player)
        mySprite7 = sprites.create(img("""
                . . . . . . . 2 . . . . . . . . 
                            . . . . . . 2 . . . . . . . . . 
                            . . . . . . . . 2 . . . . . . . 
                            . . . . . . . . 2 2 . 2 . . . . 
                            . . . . . . . 2 . 2 . . . . . . 
                            . . . . . . 2 2 5 2 2 . . . . . 
                            . . . . . . 2 4 5 2 2 . . . . . 
                            . . . . . 2 4 5 5 2 2 . . . . . 
                            . . . . . 2 5 5 4 2 . . . . . . 
                            . . . . . . 2 5 2 . . . . . . .
            """),
            SpriteKind.spell)
        mySprite7.set_position(mySprite4.x, mySprite4.y)
        mySprite8 = sprites.create(img("""
                f f f f f f f f f 
                            f 9 9 9 9 9 9 9 f 
                            f 1 9 1 9 9 9 9 f 
                            f 1 9 1 9 9 9 1 f 
                            f 1 9 1 9 9 9 1 f 
                            f 9 9 1 1 9 9 1 f 
                            f 9 9 9 9 9 1 9 f 
                            f 9 9 9 9 9 9 9 f 
                            f f f f f f f f f
            """),
            SpriteKind.spell)
        mySprite8.set_position(mySprite5.x, mySprite5.y)
        mySprite9 = sprites.create(img("""
                . . f f . f f . . 
                            . f 3 3 f 3 3 f . 
                            f 3 d 3 3 3 3 3 f 
                            f 3 3 3 3 3 3 3 f 
                            f 3 3 3 3 3 3 3 f 
                            . f 3 3 3 3 3 f . 
                            . . f 3 3 3 f . . 
                            . . . f 3 f . . . 
                            . . . . f . . . .
            """),
            SpriteKind.spell)
        mySprite9.set_position(mySprite6.x, mySprite6.y)
    elif story.check_last_answer("wizard"):
        mySprite = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . f f f f f . . . . . . . . . 
                            . f 8 8 8 8 8 f . . . . . . . . 
                            f 8 f f 8 8 8 8 f . . . . . . . 
                            8 f f 8 8 8 8 8 f . . . . . . . 
                            8 f b 8 8 8 8 8 8 f . . . . . . 
                            f b b d d f d f d 8 f . . . . . 
                            . f b b d d d d b f . . . . . . 
                            . f b b b b b b b f . . . . . . 
                            . . f b b b d b f . . . . . . . 
                            . . f 8 b b b b f . . . . . . . 
                            . f . f 8 b b 8 f f f . . . . . 
                            . f . . f b b 8 4 4 f . . . . . 
                            . f f f 8 8 b 8 f f . . . . . . 
                            f 8 8 8 8 8 b 8 8 f . . . . . . 
                            f f f f f f f f f f . . . . . .
            """),
            SpriteKind.player)
        mySprite7 = sprites.create(img("""
                . . . . . . . 2 . . . . . . . . 
                            . . . . . . 2 . . . . . . . . . 
                            . . . . . . . . 2 . . . . . . . 
                            . . . . . . . . 2 2 . 2 . . . . 
                            . . . . . . . 2 . 2 . . . . . . 
                            . . . . . . 2 2 5 2 2 . . . . . 
                            . . . . . . 2 4 5 2 2 . . . . . 
                            . . . . . 2 4 5 5 2 2 . . . . . 
                            . . . . . 2 5 5 4 2 . . . . . . 
                            . . . . . . 2 5 2 . . . . . . .
            """),
            SpriteKind.spell)
        mySprite7.set_position(mySprite4.x, mySprite4.y)
        mySprite8 = sprites.create(img("""
                . . f f . f f . . 
                            . f 3 3 f 3 3 f . 
                            f 3 d 3 3 3 3 3 f 
                            f 3 3 3 3 3 3 3 f 
                            f 3 3 3 3 3 3 3 f 
                            . f 3 3 3 3 3 f . 
                            . . f 3 3 3 f . . 
                            . . . f 3 f . . . 
                            . . . . f . . . .
            """),
            SpriteKind.spell)
        mySprite8.set_position(mySprite5.x, mySprite5.y)
        mySprite9 = sprites.create(img("""
                . . f f . f f . . 
                            . f 2 2 f 2 2 f . 
                            f 2 1 2 2 2 2 2 f 
                            f 2 2 2 9 2 2 2 f 
                            f 2 2 9 9 9 2 2 f 
                            . f 2 2 9 2 2 f . 
                            . . f 2 2 2 f . . 
                            . . . f 2 f . . . 
                            . . . . f . . . .
            """),
            SpriteKind.spell)
        mySprite9.set_position(mySprite6.x, mySprite6.y)
    else:
        mySprite = sprites.create(img("""
                . . . . . . . . . . . . . . . . 
                            . . . . . . . . . . . . . . . . 
                            . . f f f f f . . . . . . . . . 
                            . f c c c c c f . . . . . . . . 
                            f c f f c c c c f . . . . . . . 
                            c f f c c c c c f . . . . . . . 
                            c f b c c c c c c f . . . . . . 
                            f b b d d f d f d 8 f . . . . . 
                            . f b b d d d d b f . . . . . . 
                            . f b b b b b b b f . . . . . . 
                            . . f b b b d b f . . . . . . . 
                            . . f c b b b b f . . . . . . . 
                            . f . f c b b c f f f . . . . . 
                            . f . . f b b c 4 4 f . . . . . 
                            . f f f c c b c f f . . . . . . 
                            f c c c c c b c c f . . . . . . 
                            f f f f f f f f f f . . . . . .
            """),
            SpriteKind.player)
mySprite2 = sprites.create(img("""
        . . f f . f f . . 
            . f 2 2 f 2 2 f . 
            f 2 1 2 2 2 2 2 f 
            f 2 2 2 2 2 2 2 f 
            f 2 2 2 2 2 2 2 f 
            . f 2 2 2 2 2 f . 
            . . f 2 2 2 f . . 
            . . . f 2 f . . . 
            . . . . f . . . .
    """),
    SpriteKind.healthBar)
mySprite2.set_position(105, 5)
statusbar = statusbars.create(20, 4, StatusBarKind.health)
statusbar.set_position(120, 5)
statusbar.set_bar_size(100, 4)
statusbar.set_color(2, 12)
mySprite.image.flip_x()
controller.move_sprite(mySprite)
scene.camera_follow_sprite(mySprite)