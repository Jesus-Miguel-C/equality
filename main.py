projectile: Sprite = None
mySprite: Sprite = None

def on_on_overlap(sprite, otherSprite):
    otherSprite.destroy()
    info.change_life_by(-1)
    if info.life() == 1:
        mySprite.say("Last chance")
        mySprite.set_image(img("""
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . 2 2 . . . . . . . . . . .
            . . . 2 2 2 2 . . . . . . . . .
            . . . 2 . . 2 2 2 . . . . . . .
            . . . 2 . . . . 2 2 2 . . . . .
            . . . 2 . . . . . . 2 2 2 . . .
            . . . 2 . . . . . . . . 2 2 2 .
            . . . 2 . . . . . . 2 2 2 . . .
            . . . 2 . . . . 2 2 2 . . . . .
            . . . 2 . . 2 2 2 . . . . . . .
            . . . 2 2 2 2 . . . . . . . . .
            . . . 2 2 . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
            . . . . . . . . . . . . . . . .
        """))
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap)

mySprite = sprites.create(img("""
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . 7 7 . . . . . . . . . . .
        . . . 7 7 7 7 . . . . . . . . .
        . . . 7 . . 7 7 7 . . . . . . .
        . . . 7 . . . . 7 7 7 . . . . .
        . . . 7 . . . . . . 7 7 7 . . .
        . . . 7 . . . . . . . . 7 7 7 .
        . . . 7 . . . . . . 7 7 7 . . .
        . . . 7 . . . . 7 7 7 . . . . .
        . . . 7 . . 7 7 7 . . . . . . .
        . . . 7 7 7 7 . . . . . . . . .
        . . . 7 7 . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
        . . . . . . . . . . . . . . . .
    """),
    SpriteKind.player)
controller.move_sprite(mySprite, 100, 100)
mySprite.set_stay_in_screen(True)
info.set_life(3)

def on_forever():
    global projectile
    projectile = sprites.create_projectile(img("""
            . . . . . . . . . c c 8 . . . .
            . . . . . . 8 c c c f 8 c c . .
            . . . c c 8 8 f c a f f f c c .
            . . c c c f f f c a a f f c c c
            8 c c c f f f f c c a a c 8 c c
            c c c b f f f 8 a c c a a a c c
            c a a b b 8 a b c c c c c c c c
            a f c a a b b a c c c c c f f c
            a 8 f c a a c c a c a c f f f c
            c a 8 a a c c c c a a f f f 8 a
            . a c a a c f f a a b 8 f f c a
            . . c c b a f f f a b b c c 6 c
            . . . c b b a f f 6 6 a b 6 c .
            . . . c c b b b 6 6 a c c c c .
            . . . . c c a b b c c c . . . .
            . . . . . c c c c c c . . . . .
        """),
        -100,
        randint(-50, 50),
        SpriteKind.enemy)
    pause(500)
forever(on_forever)
