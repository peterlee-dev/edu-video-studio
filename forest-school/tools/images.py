"""숲 학교 사계절 — codex 로 그릴 그림 목록

- 장면 그림(scene): 곰취 선생님과 아이들이 나오는 장면. img/gen/cast.png(등장인물 기준 그림)를 같이 붙여서 생김새를 맞춰요
- 생물 그림판(panel): 생물을 왼쪽부터 한 줄로 늘어놓은 그림. 이름표는 화면 코드가 칸마다 붙여요(그림 속 글자는 넣지 않아요)
- 배경(plain): 사람 없는 풍경

  python3 tools/gen_images.py            # 없는 그림만 그려요 (img/gen/<key>.png)
  python3 tools/gen_images.py --redo sp_ginger,su_worm
"""

STYLE = ('Soft colored-pencil and watercolor picture-book illustration for young children, gentle hand-drawn ink outlines, '
         'warm natural palette, cute rounded proportions, friendly faces with simple dot eyes and rosy cheeks. '
         'Absolutely no text, no letters, no numbers, no labels, no speech bubbles anywhere in the image.')
CAST = ('The forest teacher and the children must look exactly like the characters in the attached reference sheet '
        '(teacher Gomchwi: elderly man, brown bucket hat, yellow-green vest, blue scarf, magnifier on lanyard; '
        'Seoa: long black hair, purple polka-dot jacket; Dojin: red cap, green checkered shirt; Hyunwoo: round glasses, blue-white hoodie; '
        'Uri: white cap worn backwards, color-block jacket; Nuri: yellow bucket hat, pink jacket; Jiho: light blue jacket).')
PANEL = ('Natural-history picture-book plate: the items are arranged in ONE horizontal row, left to right in exactly this order, '
         'each centered in its own equal-width column with generous empty space between them, nothing overlapping, similar visual size, '
         'isolated on a plain warm cream paper background. Accurate, recognisable details.')


def scene(desc, season, cast=True): return {'kind': 'scene', 'cast': cast, 'prompt': f'Landscape 16:9 scene. {season} {desc}'}
def plain(desc): return {'kind': 'plain', 'cast': False, 'prompt': f'Landscape 16:9 wide scene, no people. {desc}'}
def panel(*items): return {'kind': 'panel', 'cast': False, 'n': len(items), 'prompt': f'Landscape 16:9. {len(items)} items: ' + '; '.join(f'({i + 1}) {x}' for i, x in enumerate(items)) + '.'}


SPRING = 'Early spring in a Korean mountain forest, fresh pale green, soft sunlight.'
SUMMER = 'Midsummer in a lush green Korean forest valley, bright sunshine.'
AUTUMN = 'Autumn in a Korean forest with red, orange and yellow leaves.'
WINTER = 'Winter in a Korean forest, bare brown trees, cold air; the teacher and children wear warm puffer jackets, knit hats and earmuffs.'

IMAGES = {
    # ---------------- 봄 ----------------
    'sp_title': plain('Early spring Korean mountain forest seen from a hillside: a tree full of tiny fluffy yellow spicebush flowers, pink azalea bushes, '
                      'young pale green trees, a few dark green pines, a winding dirt path, two small yellow butterflies, soft blue sky with empty space at the top for a title.'),
    'sp_ginger': scene('On a winding forest path the teacher points up at a small tree with bare grey-green branches covered in tiny fluffy yellow flower clusters (Lindera obtusiloba, '
                       'flowers bloom before leaves). The children gather around looking up curiously; one child sniffs a twig.', SPRING),
    'sp_branches': panel('a branch of Korean cornelian cherry (Cornus officinalis) with rough, flaky, peeling brown bark and clusters of small yellow star-shaped flowers on short stalks',
                         'a branch of Japanese spicebush (Lindera obtusiloba) with smooth grey-green bark and round fluffy balls of tiny yellow flowers sitting tight on the twig'),
    'sp_azalea': scene('The children and the teacher stand beside big bushes of pink Korean azalea (Rhododendron mucronulatum) in full bloom; '
                       'a girl pretends to nibble a pink petal; bright yellow forsythia bushes bloom along the path behind them.', SPRING),
    'sp_flowers5': panel('hepatica (Hepatica asiatica) with small pale purple flowers and fuzzy stems', 'a purple violet (Viola mandshurica) with narrow leaves',
                         'wild ginger (Asarum sieboldii): a dark maroon cup-shaped flower at ground level under two heart-shaped leaves',
                         'whitlow grass (Draba nemorosa): a low rosette of small leaves with tiny yellow flowers on thin stems',
                         'a small wild iris (Iris rossii) with violet-blue flowers and thin grassy leaves'),
    'sp_dandelion': scene('On a sunny grassy hillside dotted with dandelions, the children blow on white dandelion seed heads; dozens of fluffy seeds float into the sky; '
                          'the teacher raises a seed head happily; backpacks are piled on the grass; a yellow butterfly flutters.', SPRING),
    'sp_pipe': scene('Close-up of three people: the teacher blows into a short hollow dandelion stem held to his lips like a little whistle; '
                     'a boy tries it too and makes a funny bitter face; a boy with glasses giggles.', SPRING),
    'sp_flowers3': panel('cinquefoil (Potentilla fragarioides) with bright yellow five-petal flowers', 'a common dandelion with a yellow flower and a white seed clock',
                         'bird\'s-eye speedwell (Veronica persica): a low plant with tiny sky-blue four-petal flowers'),
    'sp_stream': scene('At a clear shallow forest stream with mossy rocks, the children kneel on stones looking into the water: there are many round clumps of jelly-like frog eggs '
                       'with black dots and coiled tube-shaped salamander egg sacs. One barefoot girl squeals because the water is cold; a girl scoops eggs with a small sieve. '
                       'Small minnows swim in the water.', SPRING),
    'sp_eggs2': panel('a round clump of clear jelly frog eggs with many black dots inside', 'a pair of long, curled, tube-shaped clear jelly salamander egg sacs with small dots inside'),
    'sp_amphib3': panel('a brown Korean mountain frog (Rana)', 'a small brown Korean salamander (Hynobius) with a long tail', 'a bumpy brown Asian toad'),
    'sp_chain4': panel('a black-and-white magpie bird', 'a green frog', 'a green grasshopper', 'a tuft of green grass'),
    'sp_horsetail': scene('The teacher and children crouch around a patch of sandy ground where pale brown, jointed, unbranched stems with cone-shaped tips stick up '
                          '(fertile shoots of field horsetail). The children look amazed; one points.', SPRING),
    'sp_horsetail2': panel('a pale brown fertile shoot of field horsetail (Equisetum arvense) with a cone-shaped spore tip and dark jointed sheaths',
                           'a green sterile shoot of field horsetail with many thin green whorled branches, like a little bottle brush'),
    'sp_fern2': panel('young bracken fern shoots (fiddleheads) curled at the top like question marks', 'a mature green bracken fern frond, finely divided'),
    'sp_greens6': panel('shepherd\'s purse (naengi) rosette with its white root', 'wild chive (dallae): thin green leaves with small white bulbs and roots',
                        'mugwort (ssuk) young leaves, silvery underneath', 'a fat green fresh shoot of Aralia (dureup) tree bud',
                        'Ixeris (godeulppaegi) rosette with a long root', 'stringy stonecrop (dolnamul) with small fleshy leaves'),
    'sp_antlion': scene('Under a dry rocky overhang in fine sand there are several small funnel-shaped pits. The teacher digs gently with a twig while the children lean in with '
                        'a magnifying glass; a tiny ant slides down into one pit.', SPRING),
    'sp_antlion2': panel('an antlion larva: small, plump, sandy grey-brown, with big curved pointed jaws', 'an adult antlion: a slender insect with a long thin body, short clubbed antennae and four long clear net-veined wings'),
    'sp_pine': scene('A girl (Seoa) kneels on the forest floor, delighted, pointing at a tiny Korean pine seedling: a thin stem topped with a ring of needles and a pine-nut shell sitting on top like a little crown. '
                     'The teacher bends over smiling and a boy with glasses looks closely.', SPRING),
    'sp_pinetree': panel('a young Korean pine tree, about five years old, with a straight trunk and exactly five clearly separated tiers (whorls) of branches stacked one above another'),
    'sp_plog': scene('The children wear white work gloves and use long trash tongs to pick up litter in the forest: plastic bottles, plastic bags, cans, paper; '
                     'a girl holds up an old rusty frying pan in surprise; a boy tugs at a bag stuck in the ground; the teacher holds a trash bag.', SPRING),
    'sp_play': scene('Children playing in a sunny forest clearing: some balance and swap places on a fallen log, a girl throws a ring made of kudzu vine onto a stick, '
                     'a boy launches an acorn with a Y-shaped branch slingshot, others build a teepee tent from long branches, the teacher watches happily.', SPRING),
    # ---------------- 여름 ----------------
    'su_title': plain('Midsummer Korean forest valley: tall leafy trees, a clear stream running between big mossy boulders, a dragonfly in the air, white fleabane flowers, '
                      'bright blue sky with puffy clouds and empty space at the top for a title.'),
    'su_ladybug': scene('Close-up: the teacher and a boy with a white backward cap peek over big green leaves; on the leaves are spiky dark ladybug larvae, an orange ladybug pupa '
                        'and tiny green aphids. The boy is surprised.', SUMMER),
    'su_lady4': panel('a spiky dark grey and orange seven-spot ladybug larva', 'an orange seven-spot ladybug pupa attached to a leaf', 'a red seven-spot ladybug adult', 'a small cluster of tiny green aphids on a stem'),
    'su_inchworm': scene('A green inchworm (geometer caterpillar) hangs from a tree branch on a thin silk thread right in front of a girl in a yellow bucket hat who jumps back startled; '
                         'the teacher laughs kindly; other children look; a white cabbage butterfly flies nearby. Everyone wears long sleeves and long trousers.', SUMMER),
    'su_insect': panel('one large honeybee-like insect seen from directly above with wings spread wide, very clear body parts: head with two big compound eyes and three tiny simple eyes, '
                       'two antennae, mouthparts, thorax with two pairs of wings and six legs, striped abdomen; centered and filling most of the image'),
    'su_draw': scene('The children sit on the grass drawing insects on paper with pencils while rolling a big dice; their drawings are funny strange insects '
                     '(a body with butterfly wings and too many legs); the teacher laughs.', SUMMER),
    'su_meadow': scene('The children search tall summer grass for insects with a butterfly net and a clear bug box; a boy cups a long slender green grasshopper in his hands; '
                       'a girl recoils; the teacher waves from the back; a dragonfly flies over.', SUMMER),
    'su_hop4': panel('a long slender green Asian longheaded grasshopper (Acrida cinerea) with a pointed head', 'a brown band-winged grasshopper (Oedaleus) with a pale X-shaped mark on its back',
                     'a green-and-brown band-winged grasshopper (Gastrimargus) without an X mark', 'a small green pointed-head grasshopper (Atractomorpha lata) with flat sword-shaped antennae'),
    'su_bug3': panel('a long thin green stick insect that looks like a twig', 'a big golden-ringed dragonfly (Anotogaster) with black and yellow stripes and green eyes', 'a dark brown millipede with very many legs, partly curled'),
    'su_berry': scene('On a summer forest path the children pick wild berries from thorny bushes and eat them happily; one boy spits out a tasteless berry; '
                      'a girl holds a handkerchief full of red berries; a swallowtail butterfly flies by.', SUMMER),
    'su_berry4': panel('Korean wild raspberry (Rubus crataegifolius): round shiny red berries with green leaves', 'mock strawberry (Duchesnea): a small round red berry on a long creeping runner with yellow flower',
                       'Korean black raspberry (Rubus coreanus) cluster: berries turning from red to deep dark purple-black', 'Rubus parvifolius: red berries like a small bunch of grapes'),
    'su_worm': scene('On a forest slope the children and the teacher gather around a long pink earthworm on the dark soil; the teacher picks it up with a twig and a leaf, not with bare hands; '
                     'a boy says something excitedly; some children look a bit grossed out.', SUMMER),
    'su_mole': plain('A cutaway view of forest soil: above ground trees and grass; underground a network of tunnels; a velvety mole sits in a chamber next to a store room full of '
                     'curled earthworms; ant nest chambers; plant roots.'),
    'su_mole2': panel('a velvety grey-black mole with big pink digging hands', 'a White\'s thrush (scaly golden-brown ground thrush) holding an earthworm in its beak'),
    'su_creek': scene('The children wade barefoot in a shallow clear forest creek with small nets and a white basin, rolling up their trousers, searching under stones for aquatic insects; '
                      'a girl shrieks at a frog on a rock; the teacher crouches on the bank.', SUMMER),
    'su_aqua4': panel('a mayfly nymph with three tail filaments and gills on its sides', 'a caddisfly larva in a tube case made of tiny pebbles and leaf bits',
                      'a whirligig beetle: shiny black oval beetle spinning on the water surface', 'a backswimmer swimming upside down on its back with long oar-like legs'),
    'su_aqua3': panel('a giant water bug (Lethocerus deyrollei): big flat brown bug with strong grasping front legs', 'a water strider standing on the water surface with long thin legs, dimples on the water',
                      'a dobsonfly larva: long segmented body with a round head and gill filaments on its sides'),
    'su_ash': scene('By a creek pool the teacher dips a freshly bruised ash-tree twig into a white basin of water and the water around it turns bright sky-blue; '
                    'the children crowd around amazed; one is pounding bark with a small stone.', SUMMER),
    'su_reed': scene('In a wide shallow creek the children play: a tiny water wheel made of crossed grass stems spins in a little waterfall between stones, '
                     'a small boat folded from a long reed leaf floats, a boy finds black river snails on a rock, a girl splashes water.', SUMMER),
    'su_reed3': panel('Korean silvergrass (eulalia) with feathery silver-white plumes on a dry hillside', 'common reed with brown feathery plume heads beside water',
                      'Phragmites japonica (dalppuripul), a reed-like grass with long creeping runners growing between creek stones'),
    'su_trap': panel('a homemade fish trap from a clear plastic bottle with the top cut off and put back upside down, small holes and a string handle', 'a small silver minnow (pale chub)', 'two dark spiral river snails (marsh snails) on a pebble'),
    # ---------------- 가을 ----------------
    'au_title': plain('Autumn Korean mountain covered with red, orange, yellow and brown trees and a few dark green pines, a winding path, '
                      'a V-shaped flock of wild geese in a pale blue sky with empty space at the top for a title.'),
    'au_box': scene('In an autumn forest the children sit on a log shaking small paper boxes next to their ears, guessing what is inside; the teacher holds his box up; '
                    'red cornelian cherry berries hang on a tree.', AUTUMN),
    'au_fruit6': panel('a smooth acorn of Mongolian oak with a scaly shallow cap', 'a round acorn of Oriental cork oak with a shaggy curly-fringed cap',
                       'small flat dark brown seeds and a narrow pod of partridge pea (Chamaecrista)', 'a shiny brown chestnut and its spiky green burr',
                       'small dark speckled wild adzuki beans (Vigna angularis var. nipponensis) and a curled thin pod', 'ginkgo seeds: pale yellow-white oval nuts'),
    'au_nuts': scene('Children collect chestnuts, acorns and fallen fruits on a leaf-covered autumn forest floor under chestnut and oak trees; spiky chestnut burrs on the ground; '
                     'a big orb-weaver spider web between branches; the teacher picks a curled bean pod.', AUTUMN),
    'au_mush': scene('An autumn forest floor among big tree trunks and a rotting log covered with many kinds of mushrooms: orange bracket fungi, grey turkey-tail on the log, '
                     'tiny cup-shaped bird\'s-nest fungi, purple small mushrooms, puffballs, a tall parasol mushroom. The teacher and children crouch to look, not touching.', AUTUMN),
    'au_mush3': panel('bird\'s nest fungus (Cyathus): tiny brown cups with small grey egg-like spore packets inside', 'a tall parasol mushroom (Macrolepiota procera) with a big scaly cap and long stem',
                      'a smaller poisonous lookalike (Chlorophyllum-like) mushroom with a large brown scale patch in the center of its cap'),
    'au_pine': scene('Under Korean pine trees the children sit on the ground cracking pine nuts gently with stones on flat rocks; big brown pine cones lie around; '
                     'a bowl of water with floating empty nuts; a squirrel holds a cone on a branch; the teacher holds up a small butterfly brooch.', AUTUMN),
    'au_fruit2': panel('hardy kiwi (darae): small smooth green grape-sized fruits, one cut open showing green flesh and tiny black seeds like a kiwi',
                       'chocolate vine (Akebia) fruit: a plump purple pod split open showing white jelly-like flesh full of black seeds'),
    'au_tochu': scene('The teacher holds up a green Eucommia leaf that has been torn in two but the halves still hang together by many fine white rubbery threads, like magic; '
                      'two children try tearing leaves too; one is surprised.', AUTUMN),
    'au_seeds': scene('A girl in a purple polka-dot jacket looks at her pink trousers covered in many small sticky seeds and burrs; the teacher explains; '
                      'a boy touches a pink jewelweed seed pod and it bursts, seeds flying; children laugh.', AUTUMN),
    'au_seeds4': panel('Adenocaulon (myeolgachi) club-shaped sticky seeds on thin stalks', 'Oplismenus grass with tiny sticky seed spikes',
                       'Desmodium (keun-doduknom-ui-galgori) with flat seed pods shaped like a pair of glasses', 'jewelweed (Impatiens textori): pink-purple flowers and a bursting seed pod'),
    'au_leaves': scene('Under red maple and yellow ginkgo trees the teacher and children throw armfuls of fallen leaves high into the air and try to catch them; '
                       'one child lies in a soft leaf pile like a bed; another holds a big leaf mask over his face.', AUTUMN),
    'au_listen': scene('The teacher and all six children hold hands in a circle on a carpet of yellow and red fallen leaves with their eyes closed, smiling and listening; '
                       'leaves drift down; a small bird sits on a branch.', AUTUMN),
    # ---------------- 겨울 ----------------
    'wi_title': plain('Winter Korean mountain with light snow falling: bare brown deciduous trees, a few snow-dusted green pines, dry golden grass, a big grey rock, '
                      'a hawk in the grey-blue sky with empty space at the top for a title.'),
    'wi_bugs': scene('In a quiet winter forest the children search carefully under fallen leaves and on bare twigs; a cluster of many ladybugs sleeps inside a tree hollow; '
                     'a mantis egg case is stuck on a twig; the teacher whispers with a finger on his lips.', WINTER),
    'wi_bug4': panel('a foamy light-brown praying mantis egg case stuck on a twig', 'many red and orange ladybugs huddled together in a crack of tree bark',
                     'a swallowtail butterfly chrysalis attached to a twig', 'a rolled-up dry leaf tube where a caterpillar hides'),
    'wi_gall': panel('an empty light-green net-like cocoon of the Japanese silk moth (Rhodinia fugax), shaped like a small balloon hanging from a twig',
                     'a round brown insect gall on an oak twig with a tiny exit hole', 'an oval swollen insect gall on a willow twig'),
    'wi_buds': scene('The teacher and the children look closely at the tips of bare winter branches with small buds; a girl in a knit hat points at a round bud; the teacher holds a twig.', WINTER),
    'wi_bud4': panel('a spicebush twig with a round fat flower bud beside a slim pointed leaf bud', 'a magnolia twig with big fuzzy grey hairy buds like little fur coats',
                     'an oak twig with pointed buds wrapped in many overlapping brown scales', 'an ash twig tip with dark buds above a horseshoe-shaped leaf scar, like a crowned little face'),
    'wi_sleep': plain('A cozy cutaway underground burrow under snowy ground: a chipmunk curled up asleep next to a pile of stored acorns and chestnuts; '
                      'and in a separate cave a big Asiatic black bear sleeping. Snow on the surface above.'),
    'wi_awake4': panel('a wild boar', 'a Korean water deer (gorani) with small tusks and no antlers', 'a grey-brown Eurasian red squirrel with ear tufts', 'a brown mountain hare'),
    'wi_tracks': scene('In a bare winter forest the children follow a line of animal footprints and hoof prints across the leaf-covered ground; a boy with glasses bends down to look; '
                       'a squirrel watches from a tree trunk.', WINTER),
    'wi_food2': panel('a Korean water deer nibbling winter buds and twigs from a low bare shrub', 'a wild boar digging in the soil with its snout, eating earthworms, grubs and a long kudzu root'),
    'wi_nest': scene('The children and the teacher look up at bare winter trees: a small cup-shaped bird nest sits in a branch fork; far away a round dark ball of mistletoe grows high on a tree '
                     'like a nest; a woodpecker hole in a trunk.', WINTER),
    'wi_nest3': panel('a small round bowl-shaped bird nest woven from twigs and stems in a branch fork', 'a big flat platform nest of dry sticks on top of a tall tree with a grey heron standing on it',
                      'a round green ball of mistletoe growing on a bare tree branch'),
    'wi_wood': panel('a great spotted woodpecker (black, white and red) clinging to a tree trunk and pecking a hole', 'a cute Siberian flying squirrel with huge dark eyes peeking out of a round tree hole'),
    'wi_lever': scene('Snow falls. The teacher and children work together to lift a heavy fallen dead log off a small young tree it was crushing: they use a long branch as a lever over a rock, '
                      'others pull a rope like tug-of-war, everyone shouting together.', WINTER),
    'wi_ice': scene('A frozen forest stream covered in snow becomes an ice slide: children slide down happily on their bottoms; others hold up thin sheets of ice with red maple leaves '
                    'frozen inside like art and look through the ice; the teacher calls out to be careful.', WINTER),
    'wi_end': scene('In a snowy forest at sunset the six children cheer with thumbs up and raised arms around the smiling teacher; gentle snowflakes; warm pink sky.', WINTER),
}
