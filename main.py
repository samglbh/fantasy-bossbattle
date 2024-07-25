namespace SpriteKind {
    export const healthBar = SpriteKind.create()
    export const magicBar = SpriteKind.create()
    export const slot1 = SpriteKind.create()
    export const slot2 = SpriteKind.create()
    export const slot3 = SpriteKind.create()
    export const spell = SpriteKind.create()
}
function level1 (mySprite: Sprite) {
    scene.setBackgroundImage(img`
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7776677777777767777777777777777777777777777667777777776777777777777777777777777777766777777777677777777777777777777777777776677777777767777777777777777777777777
        7666777777777667777777777777777777777767766677777777766777777777777777777777776776667777777776677777777777777777777777677666777777777667777777777777777777777767
        7767766777667766777766777777777777777766776776677766776677776677777777777777776677677667776677667777667777777777777777667767766777667766777766777777777777777766
        6666667767766766776766777777777777776676666666776776676677676677777777777777667666666677677667667767667777777777777766766666667767766766776766777777777777776676
        6666677766766666766667777777777777666677666667776676666676666777777777777766667766666777667666667666677777777777776666776666677766766666766667777777777777666677
        6666676666666676666677767777776667776667666667666666667666667776777777666777666766666766666666766666777677777766677766676666676666666676666677767777776667776667
        6666666666666776677666667766677766777666666666666666677667766666776667776677766666666666666667766776666677666777667776666666666666666776677666667766677766777666
        6666666666666766667766677677667766666666666666666666676666776667767766776666666666666666666667666677666776776677666666666666666666666766667766677677667766666666
        66b666666666666666666667667776676666666666b666666666666666666667667776676666666666b666666666666666666667667776676666666666b6666666666666666666676677766766666666
        66b6666666666666666666666b6776666666666666b6666666666666666666666b6776666666666666b6666666666666666666666b6776666666666666b6666666666666666666666b67766666666666
        66b6666666666666666666666bb676666666666666b6666666666666666666666bb676666666666666b6666666666666666666666bb676666666666666b6666666666666666666666bb6766666666666
        66b66666669bb666666669966bbb66666666666666b66666669bb666666669966bbb66666666666666b66666669bb666666669966bbb66666666666666b66666669bb666666669966bbb666666666666
        66b66666699cbb666666cc9666bb66666666666666b666666999bb666666999666bb66666666666666b666666999bb666666999666bb66666666666666b666666999bb666666999666bb666666666666
        6bb6669669966bbb69666c9966bb6666666666666bb6669669966bbb69666c9966bb6666666666666bb6669669966bbb69666c9966bb6666666666666bb6669669966bbb69666c9966bb666666666666
        6bb666c96696c9bbb9966c9966bbb666666666666bb666c96696c9bbb9966c9966bbb666666666666bb666c96696c9bbb9966c9966bbb666666666666bb666c96696c9bbb9966c9966bbb66666666666
        6bb66cc9999c996bb99ccc96666bb666666666666bb66cc9999c996bb99ccc96666bb666666666666bb66cc9999c996bb99ccc96666bb666666666666bb66cc9999c996bb99ccc96666bb66666666666
        bbb666c9999c996bb99cc99669cbbb6696666666bbb666c9999c996bb99cc99669cbbb6696666666bbb666c9999c996bb99cc99669cbbb6696666666bbb666c9999c996bb99cc99669cbbb6696666666
        bbbcc6c9999c999bbb9cc999996bbb6699966666bbbcc6c9999c999bbb9cc999996bbb6699966666bbbcc6c9999c999bbb9cc999996bbb6699966666bbbcc6c9999c999bbb9cc999996bbb6699966666
        bbb6ccc9999c9999bb9cc9999c6bbb9699666666bbb6ccc9999c9999bb9cc9999c6bbb9699666666bbb6ccc9999c9999bb9cc9999c6bbb9699666666bbb6ccc9999c9999bb9cc9999c6bbb9699666666
        bbb6ccc999c99999bbbcc9999c9bbb9999669966bbb6ccc999c99999bbbcc9999c9bbb9999669966bbb6ccc999c99999bbbcc9999c9bbb9999669966bbb6ccc999c99999bbbcc9999c9bbb9999669966
        bbbcccc999c999999bbcc9999c9bbbb9999c9996bbbcccc999c999999bbcc9999c9bbbb9999c9996bbbcccc999c999999bbcc9999c9bbbb9999c9996bbbcccc999c999999bbcc9999c9bbbb9999c9996
        bb9cccc99cc9999999bb9999cc9bbbb9999c9999bb9cccc99cc9999999bb9999cc9bbbb9999c9999bb9cccc99cc9999999bb9999cc9bbbb9999c9999bb9cccc99cc9999999bb9999cc9bbbb9999c9999
        bb99ccccc999999999bbb999c999bbb9999c9999bb99ccccc999999999bbb999c999bbb9999c9999bb99ccccc999999999bbb999c999bbb9999c9999bb99ccccc999999999bbb999c999bbb9999c9999
        bb99cccc9999999999cbbbbcc999bbb9999c999bbb99cccc9999999999cbbbbcc999bbb9999c999bbb99cccc9999999999cbbbbcc999bbb9999c999bbb99cccc9999999999cbbbbcc999bbb9999c999b
        bb99ccc99999999999ccbbbb9999bbbb999c999bbb99ccc99999999999ccbbbb9999bbbb999c999bbb99ccc99999999999ccbbbb9999bbbb999c999bbb99ccc99999999999ccbbbb9999bbbb999c999b
        bb99ccc99999999999ccbbbbbb99bbbb999c999bbb99ccc99999999999ccbbbbbb99bbbb999c999bbb99ccc99999999999ccbbbbbb99bbbb999c999bbb99ccc99999999999ccbbbbbb99bbbb999c999b
        b9999cc9999999999ccccbbbbbbbbbbbb999c99bb9999cc9999999999ccccbbbbbbbbbbbb999c99bb9999cc9999999999ccccbbbbbbbbbbbb999c99bb9999cc9999999999ccccbbbbbbbbbbbb999c99b
        b9999ccc999999999cc99999bbbbbbbbb999c99bb9999ccc999999999cc99999bbbbbbbbb999c99bb9999ccc999999999cc99999bbbbbbbbb999c99bb9999ccc999999999cc99999bbbbbbbbb999c99b
        b9999cccc99999999cc999999bbbbbbbb999c9bbb9999cccc99999999cc999999bbbbbbbb999c9bbb9999cccc99999999cc999999bbbbbbbb999c9bbb9999cccc99999999cc999999bbbbbbbb999c9bb
        b9999ccccc999999ccc9999999bbbbbbb999cbbbb9999ccccc999999ccc9999999bbbbbbb999cbbbb9999ccccc999999ccc9999999bbbbbbb999cbbbb9999ccccc999999ccc9999999bbbbbbb999cbbb
        cc99999ccccc9999ccc999999999bbbbb999bbbbcc99999ccccc9999ccc999999999bbbbb999bbbbcc99999ccccc9999ccc999999999bbbbb999bbbbcc99999ccccc9999ccc999999999bbbbb999bbbb
        9c99999ccccccc9ccc9999999999bbbbb99bbbb99c99999ccccccc9ccc9999999999bbbbb99bbbb99c99999ccccccc9ccc9999999999bbbbb99bbbb99c99999ccccccc9ccc9999999999bbbbb99bbbb9
        9c999999cccccccccc9999999999bbbbb99bbb999c999999cccccccccc9999999999bbbbb99bbb999c999999cccccccccc9999999999bbbbb99bbb999c999999cccccccccc9999999999bbbbb99bbb99
        9c999999ccccccccc99999999999bbbbb99bb9999c999999ccccccccc99999999999bbbbb99bb9999c999999ccccccccc99999999999bbbbb99bb9999c999999ccccccccc99999999999bbbbb99bb999
        9cc99999ccccccc9999999999999bbbbb99bbc999cc99999ccccccc9999999999999bbbbb99bbc999cc99999ccccccc9999999999999bbbbb99bbc999cc99999ccccccc9999999999999bbbbb99bbc99
        99cc9999cccccc99999999999999bbbbb99bbc9999cc9999cccccc99999999999999bbbbb99bbc9999cc9999cccccc99999999999999bbbbb99bbc9999cc9999cccccc99999999999999bbbbb99bbc99
        99ccc999cccccc99999999999999bbbbb9bbbcc999ccc999cccccc99999999999999bbbbb9bbbcc999ccc999cccccc99999999999999bbbbb9bbbcc999ccc999cccccc99999999999999bbbbb9bbbcc9
        9999cccccccccc9999999999999bbbbbb9bbb9c99999cccccccccc9999999999999bbbbbb9bbb9c99999cccccccccc9999999999999bbbbbb9bbb9c99999cccccccccc9999999999999bbbbbb9bbb9c9
        9999cccccccccc9999999999999bbbbbbbbb99c99999cccccccccc9999999999999bbbbbbbbb99c99999cccccccccc9999999999999bbbbbbbbb99c99999cccccccccc9999999999999bbbbbbbbb99c9
        999999cccccccc9999999999999bbbbbbbbb99cc999999cccccccc9999999999999bbbbbbbbb99cc999999cccccccc9999999999999bbbbbbbbb99cc999999cccccccc9999999999999bbbbbbbbb99cc
        d9999999cccccc999999999999bbbbbbbbb9999cc9999999cccccc999999999999bbbbbbbbb9999cc9999999cccccc999999999999bbbbbbbbb9999cc9999999cccccc999999999999bbbbbbbbb9999c
        dd9999999ccccc999999999999bbbbbbbbb99999cc9999999ccccc999999999999bbbbbbbbb99999cc9999999ccccc999999999999bbbbbbbbb99999cc9999999ccccc999999999999bbbbbbbbb99999
        dd9999999ccccc999999999999bbbbbbbb999999cc9999999ccccc999999999999bbbbbbbb999999cc9999999ccccc999999999999bbbbbbbb999999cc9999999ccccc999999999999bbbbbbbb999999
        9d9999999ccccc99999999999bbbbbbbbb9999999c9999999ccccc99999999999bbbbbbbbb9999999c9999999ccccc99999999999bbbbbbbbb9999999c9999999ccccc99999999999bbbbbbbbb999999
        9d9999999ccccc99999999999bbbbbbbbb9999999c9999999ccccc99999999999bbbbbbbbb9999999c9999999ccccc99999999999bbbbbbbbb9999999c9999999ccccc99999999999bbbbbbbbb999999
        9d9999999ccccc99999999999bbbbbbbbb9999999c9999999ccccc99999999999bbbbbbbbb9999999c9999999ccccc99999999999bbbbbbbbb9999999c9999999ccccc99999999999bbbbbbbbb999999
        9d9999999ccccc99999999999bbbbbbbbb9999999c9999999ccccc99999999999bbbbbbbbb9999999c9999999ccccc99999999999bbbbbbbbb9999999c9999999ccccc99999999999bbbbbbbbb999999
        9dd999999ccccc99999999999bbbbbbbb99999999cc999999ccccc99999999999bbbbbbbb99999999cc999999ccccc99999999999bbbbbbbb99999999cc999999ccccc99999999999bbbbbbbb9999999
        9dd999999ccccc99999999999bbbbbbbb99999999cc999999ccccc99999999999bbbbbbbb99999999cc999999ccccc99999999999bbbbbbbb99999999cc999999ccccc99999999999bbbbbbbb9999999
        ddd999999ccccc99999999999bbbbbbbb9999999ccc999999ccccc99999999999bbbbbbbb9999999ccc999999ccccc99999999999bbbbbbbb9999999ccc999999ccccc99999999999bbbbbbbb9999999
        dd9999999ccccc99999999999bbbbbbbb9999999cc9999999ccccc99999999999bbbbbbbb9999999cc9999999ccccc99999999999bbbbbbbb9999999cc9999999ccccc99999999999bbbbbbbb9999999
        dd9999999cccccc9999999999bbbbbbbb9999999cc9999999cccccc9999999999bbbbbbbb9999999cc9999999cccccc9999999999bbbbbbbb9999999cc9999999cccccc9999999999bbbbbbbb9999999
        dd9999999cccccc9999999999bbbbbbbb9999999cc9999999cccccc9999999999bbbbbbbb9999999cc9999999cccccc9999999999bbbbbbbb9999999cc9999999cccccc9999999999bbbbbbbb9999999
        dd9999999cccccc9999999999bbbbbbb99999999cc9999999cccccc9999999999bbbbbbb99999999cc9999999cccccc9999999999bbbbbbb99999999cc9999999cccccc9999999999bbbbbbb99999999
        d99999999cccccc9999999999bbbbbbb9999999cc99999999cccccc9999999999bbbbbbb9999999cc99999999cccccc9999999999bbbbbbb9999999cc99999999cccccc9999999999bbbbbbb9999999c
        d99999999cccccc9999999999bbbbbbb999999ccc99999999cccccc9999999999bbbbbbb999999ccc99999999cccccc9999999999bbbbbbb999999ccc99999999cccccc9999999999bbbbbbb999999cc
        d99999999cccccc9999999999bbbbbbb999999ccc99999999cccccc9999999999bbbbbbb999999ccc99999999cccccc9999999999bbbbbbb999999ccc99999999cccccc9999999999bbbbbbb999999cc
        999999999ccccccc999999999bbbbbbb99999ccc999999999ccccccc999999999bbbbbbb99999ccc999999999ccccccc999999999bbbbbbb99999ccc999999999ccccccc999999999bbbbbbb99999ccc
        999999999ccccccc999999999bbbbbbb99999ccc999999999ccccccc999999999bbbbbbb99999ccc999999999ccccccc999999999bbbbbbb99999ccc999999999ccccccc999999999bbbbbbb99999ccc
        999999999ccccccc999999999bbbbbbb99999ccc999999999ccccccc999999999bbbbbbb99999ccc999999999ccccccc999999999bbbbbbb99999ccc999999999ccccccc999999999bbbbbbb99999ccc
        999999999cccccccc99999999bbbbbbb9999cccc999999999cccccccc99999999bbbbbbb9999cccc999999999cccccccc99999999bbbbbbb9999cccc999999999cccccccc99999999bbbbbbb9999cccc
        999999999cccccccc99999999bbbbbbb9999cccc999999999cccccccc99999999bbbbbbb9999cccc999999999cccccccc99999999bbbbbbb9999cccc999999999cccccccc99999999bbbbbbb9999cccc
        999999999cccccccc99999999bbbbbbb9999ccc9999999999cccccccc99999999bbbbbbb9999ccc9999999999cccccccc99999999bbbbbbb9999ccc9999999999cccccccc99999999bbbbbbb9999ccc9
        9999999999cccccccc999999bbbbbbbb9999ccc99999999999cccccccc999999bbbbbbbb9999ccc99999999999cccccccc999999bbbbbbbb9999ccc99999999999cccccccc999999bbbbbbbb9999ccc9
        c999999999cccccccc999999bbbbbbbbccccccccc999999999cccccccc999999bbbbbbbbccccccccc999999999cccccccc999999bbbbbbbbccccccccc999999999cccccccc999999bbbbbbbbcccccccc
        ccccc99999cccccccc999999bbbbbbbbbcccccccccccc99999cccccccc999999bbbbbbbbbcccccccccccc99999cccccccc999999bbbbbbbbbcccccccccccc99999cccccccc999999bbbbbbbbbccccccc
        cccccccc99ccccccccc999ccbbbbbbbbbccccccccccccccc99ccccccccc999ccbbbbbbbbbccccccccccccccc99ccccccccc999ccbbbbbbbbbccccccccccccccc99ccccccccc999ccbbbbbbbbbccccccc
        ccccccccccccccccccc9ccccbbbbbbbbbcccccccccccccccccccccccccc9ccccbbbbbbbbbcccccccccccccccccccccccccc9ccccbbbbbbbbbcccccccccccccccccccccccccc9ccccbbbbbbbbbccccccc
        ccccccccccccccccccccccccbbbbbbbbbbccccccccccccccccccccccccccccccbbbbbbbbbbccccccccccccccccccccccccccccccbbbbbbbbbbccccccccccccccccccccccccccccccbbbbbbbbbbcccccc
        ccccccccccccccccccccccccbbbbbbbbbbccccccccccccccccccccccccccccccbbbbbbbbbbccccccccccccccccccccccccccccccbbbbbbbbbbccccccccccccccccccccccccccccccbbbbbbbbbbcccccc
        cccccccccccccccccccccccbbbbbbbbbbbcccccccccccccccccccccccccccccbbbbbbbbbbbcccccccccccccccccccccccccccccbbbbbbbbbbbcccccccccccccccccccccccccccccbbbbbbbbbbbcccccc
        cccccccccccccccccccccccbbbbbbbbbbbbccccccccccccccccccccccccccccbbbbbbbbbbbbccccccccccccccccccccccccccccbbbbbbbbbbbbccccccccccccccccccccccccccccbbbbbbbbbbbbccccc
        cccccccccccccccccccccccbbbbbbbbbbbbccccccccccccccccccccccccccccbbbbbbbbbbbbccccccccccccccccccccccccccccbbbbbbbbbbbbccccccccccccccccccccccccccccbbbbbbbbbbbbccccc
        cccccccccccccccccccccccbbbbbbbbbbbbccccccccccccccccccccccccccccbbbbbbbbbbbbccccccccccccccccccccccccccccbbbbbbbbbbbbccccccccccccccccccccccccccccbbbbbbbbbbbbccccc
        cccccccccccccccccccccccbbbbbbbbbbbbccccccccccccccccccccccccccccbbbbbbbbbbbbccccccccccccccccccccccccccccbbbbbbbbbbbbccccccccccccccccccccccccccccbbbbbbbbbbbbccccc
        ccccccccccccccccccc7777777777bbbbbbcccccccccccccccccccccccc7777777777bbbbbbcccccccccccccccccccccccc7777777777bbbbbbcccccccccccccccccccccccc7777777777bbbbbbccccc
        cccccccccccccc77777777777777777777bccccccccccccccccccc77777777777777777777bccccccccccccccccccc77777777777777777777bccccccccccccccccccc77777777777777777777bccccc
        ccccccccccc7777777777777777777777777ccccccccccccccc7777777777777777777777777ccccccccccccccc7777777777777777777777777ccccccccccccccc7777777777777777777777777cccc
        cccccccc777777777777777777777777777777cccccccccc777777777777777777777777777777cccccccccc777777777777777777777777777777cccccccccc777777777777777777777777777777cc
        ccccc77777777777777777777777777777777777ccccc77777777777777777777777777777777777ccccc77777777777777777777777777777777777ccccc77777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        7777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777777
        `)
    mySprite.setPosition(26, 86)
    mySprite10 = sprites.create(img`
        . . . . . . . . . . . . . . . . 
        . . . . c c c c . . . . . . . . 
        . . c c 9 9 9 9 c c . . . . . . 
        . c 9 9 9 9 9 9 9 9 c . . . . . 
        c 9 9 9 9 9 1 f 9 9 9 c . . . . 
        c 9 9 9 9 9 f f 9 9 9 9 c . . . 
        c 9 9 9 9 9 9 9 9 9 9 9 c . . . 
        c c b b 1 b 9 9 9 9 9 9 d c . . 
        c 9 3 3 3 9 9 9 9 9 d d d c . . 
        . b 9 9 9 9 9 9 9 9 d d d c . . 
        . . c b b c 9 9 b d d d d c c . 
        . c b b c 9 9 b b d d d d c d c 
        . c c c c c c d d d d d d d d c 
        . . . c c c c d 9 9 b d d d c . 
        . . c c c c c b 9 9 b c c c . . 
        . . c b b b c d 9 9 b c . . . . 
        `, SpriteKind.Enemy)
    mySprite10.setPosition(108, 86)
    projectile = sprites.createProjectileFromSprite(img`
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . 8 9 9 9 8 8 8 . . . . . 
        . . . 8 9 1 1 1 1 1 9 9 8 8 8 . 
        . . . 8 1 1 1 1 1 1 1 1 1 1 1 . 
        . . . 8 9 1 1 1 1 1 9 9 8 8 8 . 
        . . . . 8 9 9 9 9 8 8 . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        `, mySprite10, 0, 50)
    battle(mySprite, mySprite10)
}
function battle (mySprite: Sprite, mySprite2: Sprite) {
    turn(isWiz)
}
function turn (bool: boolean) {
    if (bool == true) {
        story.printDialog("buff phase", 80, 100, 50, 150)
        if (mySprite.image == img`
            . . . . . . . . . . . . . . . . 
            . . . . . . . . . . . . . . . . 
            . . f f f f f . . . . . . . . . 
            . f c c c c c f . . . . . . . . 
            f c f f c c c c f . . . . . . . 
            c f f c c c c c f . . . . . . . 
            c f b c c c c c c f . . . . . . 
            f b b d d f d f d c f . . . . . 
            . f b b d d d d b f . . . . . . 
            . f b b b b b b b f . . . . . . 
            . . f b b b d b f . . . . . . . 
            . . f c b b b b f . . . . . . . 
            . f . f c b b c f f f . . . . . 
            . f . . f b b c 4 4 f . . . . . 
            . f f f c c b c f f . . . . . . 
            f c c c c c b c c f . . . . . . 
            f f f f f f f f f f . . . . . . 
            ` || mySprite.image == img`
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
            `) {
            pauseUntil(() => controller.B.isPressed() || controller.A.isPressed())
            if (controller.A.isPressed()) {
                if (mySprite8.image == img`
                    . . f f . f f . . 
                    . f 3 3 f 3 3 f . 
                    f 3 d 3 3 3 3 3 f 
                    f 3 3 3 3 3 3 3 f 
                    f 3 3 3 3 3 3 3 f 
                    . f 3 3 3 3 3 f . 
                    . . f 3 3 3 f . . 
                    . . . f 3 f . . . 
                    . . . . f . . . . 
                    ` || mySprite8.image == img`
                    . . f f . f f . . 
                    . f 2 2 f 2 2 f . 
                    f 2 1 2 2 2 2 2 f 
                    f 2 2 2 9 2 2 2 f 
                    f 2 2 9 9 9 2 2 f 
                    . f 2 2 9 2 2 f . 
                    . . f 2 2 2 f . . 
                    . . . f 2 f . . . 
                    . . . . f . . . . 
                    `) {
                    if (mySprite8.image == img`
                        . . f f . f f . . 
                        . f 3 3 f 3 3 f . 
                        f 3 d 3 3 3 3 3 f 
                        f 3 3 3 3 3 3 3 f 
                        f 3 3 3 3 3 3 3 f 
                        . f 3 3 3 3 3 f . 
                        . . f 3 3 3 f . . 
                        . . . f 3 f . . . 
                        . . . . f . . . . 
                        `) {
                        statusbar3.value += 10
                        statusbar2.value += -10
                    } else if (mySprite8.image == img`
                        . . f f . f f . . 
                        . f 2 2 f 2 2 f . 
                        f 2 1 2 2 2 2 2 f 
                        f 2 2 2 9 2 2 2 f 
                        f 2 2 9 9 9 2 2 f 
                        . f 2 2 9 2 2 f . 
                        . . f 2 2 2 f . . 
                        . . . f 2 f . . . 
                        . . . . f . . . . 
                        `) {
                        statusbar3.value += 10
                        statusbar2.value += 10
                        statusbar2.value += -5
                    }
                } else if (mySprite9.image == img`
                    . . f f . f f . . 
                    . f 2 2 f 2 2 f . 
                    f 2 1 2 2 2 2 2 f 
                    f 2 2 2 9 2 2 2 f 
                    f 2 2 9 9 9 2 2 f 
                    . f 2 2 9 2 2 f . 
                    . . f 2 2 2 f . . 
                    . . . f 2 f . . . 
                    . . . . f . . . . 
                    ` || mySprite9.image == img`
                    . . f f . f f . . 
                    . f 3 3 f 3 3 f . 
                    f 3 d 3 3 3 3 3 f 
                    f 3 3 3 3 3 3 3 f 
                    f 3 3 3 3 3 3 3 f 
                    . f 3 3 3 3 3 f . 
                    . . f 3 3 3 f . . 
                    . . . f 3 f . . . 
                    . . . . f . . . . 
                    `) {
                    if (mySprite9.image == img`
                        . . f f . f f . . 
                        . f 3 3 f 3 3 f . 
                        f 3 d 3 3 3 3 3 f 
                        f 3 3 3 3 3 3 3 f 
                        f 3 3 3 3 3 3 3 f 
                        . f 3 3 3 3 3 f . 
                        . . f 3 3 3 f . . 
                        . . . f 3 f . . . 
                        . . . . f . . . . 
                        `) {
                    	
                    } else if (mySprite9.image == img`
                        . . f f . f f . . 
                        . f 2 2 f 2 2 f . 
                        f 2 1 2 2 2 2 2 f 
                        f 2 2 2 9 2 2 2 f 
                        f 2 2 9 9 9 2 2 f 
                        . f 2 2 9 2 2 f . 
                        . . f 2 2 2 f . . 
                        . . . f 2 f . . . 
                        . . . . f . . . . 
                        `) {
                    	
                    }
                }
            } else {
            	
            }
        } else {
        	
        }
    } else {
    	
    }
}
let projectile: Sprite = null
let mySprite10: Sprite = null
let list: Sprite[] = []
let mySprite9: Sprite = null
let mySprite8: Sprite = null
let mySprite7: Sprite = null
let statusbar3: StatusBarSprite = null
let mySprite6: Sprite = null
let mySprite5: Sprite = null
let mySprite4: Sprite = null
let statusbar2: StatusBarSprite = null
let mySprite3: Sprite = null
let isWiz = false
let mySprite: Sprite = null
let name = game.askForString("name", 12)
story.printDialog("choose a class", 80, 100, 50, 150)
story.showPlayerChoices("mage", "warrior")
story.printDialog("choose a subclass", 80, 100, 50, 150)
if (story.checkLastAnswer("warrior")) {
    story.showPlayerChoices("barbarian", "ranger", "rogue")
    if (story.checkLastAnswer("barbarian")) {
        mySprite = sprites.create(img`
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
            `, SpriteKind.Player)
    } else if (story.checkLastAnswer("ranger")) {
        mySprite = sprites.create(img`
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
            `, SpriteKind.Player)
    } else {
        mySprite = sprites.create(img`
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
            `, SpriteKind.Player)
    }
    isWiz = false
} else {
    isWiz = true
    mySprite3 = sprites.create(img`
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
        `, SpriteKind.magicBar)
    mySprite3.setPosition(105, 15)
    statusbar2 = statusbars.create(20, 4, StatusBarKind.Magic)
    statusbar2.setPosition(120, 15)
    statusbar2.setBarSize(100, 4)
    statusbar2.setColor(6, 12)
    mySprite4 = sprites.create(img`
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
        `, SpriteKind.slot1)
    mySprite5 = sprites.create(img`
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
        `, SpriteKind.slot2)
    mySprite6 = sprites.create(img`
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
        `, SpriteKind.slot3)
    mySprite4.setPosition(50, 15)
    mySprite5.setPosition(30, 15)
}
let mySprite2 = sprites.create(img`
    . . f f . f f . . 
    . f 2 2 f 2 2 f . 
    f 2 1 2 2 2 2 2 f 
    f 2 2 2 2 2 2 2 f 
    f 2 2 2 2 2 2 2 f 
    . f 2 2 2 2 2 f . 
    . . f 2 2 2 f . . 
    . . . f 2 f . . . 
    . . . . f . . . . 
    `, SpriteKind.healthBar)
mySprite2.setPosition(105, 5)
statusbar3 = statusbars.create(20, 4, StatusBarKind.Health)
statusbar3.setPosition(120, 5)
statusbar3.setBarSize(100, 4)
statusbar3.setColor(2, 12)
mySprite6.setPosition(70, 15)
story.showPlayerChoices("warlock", "wizard", "cleric")
if (story.checkLastAnswer("warlock")) {
    mySprite = sprites.create(img`
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . f f f f f . . . . . . . . . 
        . f a a a a a f . . . . . . . . 
        f a f f a a a a f . . . . . . . 
        a f f a a a a a f . . . . . . . 
        a f b a a a a a a f . . . . . . 
        f b b d d f d f d a f . . . . . 
        . f b b d d d d b f . . . . . . 
        . f b b b b b b b f . . . . . . 
        . . f b b b d b f . . . . . . . 
        . . f a b b b b f . . . . . . . 
        . f . f a b b a f f f . . . . . 
        . f . . f b b a 4 4 f . . . . . 
        . f f f a a b a f f . . . . . . 
        f a a a a a b a a f . . . . . . 
        f f f f f f f f f f . . . . . . 
        `, SpriteKind.Player)
    mySprite7 = sprites.create(img`
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
        `, SpriteKind.spell)
    mySprite7.setPosition(mySprite4.x, mySprite4.y)
    mySprite8 = sprites.create(img`
        f f f f f f f f f 
        f 9 9 9 9 9 9 9 f 
        f 1 9 1 9 9 9 9 f 
        f 1 9 1 9 9 9 1 f 
        f 1 9 1 9 9 9 1 f 
        f 9 9 1 1 9 9 1 f 
        f 9 9 9 9 9 1 9 f 
        f 9 9 9 9 9 9 9 f 
        f f f f f f f f f 
        `, SpriteKind.spell)
    mySprite8.setPosition(mySprite5.x, mySprite5.y)
    mySprite9 = sprites.create(img`
        . . f f . f f . . 
        . f 3 3 f 3 3 f . 
        f 3 d 3 3 3 3 3 f 
        f 3 3 3 3 3 3 3 f 
        f 3 3 3 3 3 3 3 f 
        . f 3 3 3 3 3 f . 
        . . f 3 3 3 f . . 
        . . . f 3 f . . . 
        . . . . f . . . . 
        `, SpriteKind.spell)
    mySprite9.setPosition(mySprite6.x, mySprite6.y)
    list = [mySprite7, mySprite8, mySprite9]
} else if (story.checkLastAnswer("wizard")) {
    mySprite = sprites.create(img`
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
        `, SpriteKind.Player)
    mySprite7 = sprites.create(img`
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
        `, SpriteKind.spell)
    mySprite7.setPosition(mySprite4.x, mySprite4.y)
    mySprite8 = sprites.create(img`
        . . f f . f f . . 
        . f 3 3 f 3 3 f . 
        f 3 d 3 3 3 3 3 f 
        f 3 3 3 3 3 3 3 f 
        f 3 3 3 3 3 3 3 f 
        . f 3 3 3 3 3 f . 
        . . f 3 3 3 f . . 
        . . . f 3 f . . . 
        . . . . f . . . . 
        `, SpriteKind.spell)
    mySprite8.setPosition(mySprite5.x, mySprite5.y)
    mySprite9 = sprites.create(img`
        . . f f . f f . . 
        . f 2 2 f 2 2 f . 
        f 2 1 2 2 2 2 2 f 
        f 2 2 2 9 2 2 2 f 
        f 2 2 9 9 9 2 2 f 
        . f 2 2 9 2 2 f . 
        . . f 2 2 2 f . . 
        . . . f 2 f . . . 
        . . . . f . . . . 
        `, SpriteKind.spell)
    mySprite9.setPosition(mySprite6.x, mySprite6.y)
    list = [mySprite7, mySprite8, mySprite9]
} else {
    mySprite = sprites.create(img`
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
        `, SpriteKind.Player)
    mySprite7 = sprites.create(img`
        . . f f . f f . . 
        . f 2 2 f c c f . 
        f 2 1 2 4 c c c f 
        f 2 2 2 4 c c c f 
        f 2 2 2 4 c c c f 
        . f 2 2 4 c c f . 
        . . f 2 4 c f . . 
        . . . f 4 f . . . 
        . . . . f . . . . 
        `, SpriteKind.spell)
    mySprite7.setPosition(mySprite4.x, mySprite4.y)
    mySprite8 = sprites.create(img`
        . . f f . f f . . 
        . f 3 3 f 3 3 f . 
        f 3 d 3 3 3 3 3 f 
        f 3 3 3 3 3 3 3 f 
        f 3 3 3 3 3 3 3 f 
        . f 3 3 3 3 3 f . 
        . . f 3 3 3 f . . 
        . . . f 3 f . . . 
        . . . . f . . . . 
        `, SpriteKind.spell)
    mySprite8.setPosition(mySprite5.x, mySprite5.y)
    mySprite9 = sprites.create(img`
        . . f f . f f . . 
        . f 2 2 f 2 2 f . 
        f 2 1 2 2 2 2 2 f 
        f 2 2 2 9 2 2 2 f 
        f 2 2 9 9 9 2 2 f 
        . f 2 2 9 2 2 f . 
        . . f 2 2 2 f . . 
        . . . f 2 f . . . 
        . . . . f . . . . 
        `, SpriteKind.spell)
    mySprite9.setPosition(mySprite6.x, mySprite6.y)
    list = [mySprite7, mySprite8, mySprite9]
}
level1(mySprite)
