# type: ignore

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cards(models.Model):
    artist = models.TextField(blank=True, null=True)
    asciiname = models.TextField(db_column='asciiName', blank=True, null=True)  # Field name made lowercase.
    availability = models.TextField(blank=True, null=True)
    boostertypes = models.TextField(db_column='boosterTypes', blank=True, null=True)  # Field name made lowercase.
    bordercolor = models.TextField(db_column='borderColor', blank=True, null=True)  # Field name made lowercase.
    cardkingdometchedid = models.TextField(db_column='cardKingdomEtchedId', blank=True, null=True)  # Field name made lowercase.
    cardkingdomfoilid = models.TextField(db_column='cardKingdomFoilId', blank=True, null=True)  # Field name made lowercase.
    cardkingdomid = models.TextField(db_column='cardKingdomId', blank=True, null=True)  # Field name made lowercase.
    cardparts = models.TextField(db_column='cardParts', blank=True, null=True)  # Field name made lowercase.
    coloridentity = models.TextField(db_column='colorIdentity', blank=True, null=True)  # Field name made lowercase.
    colorindicator = models.TextField(db_column='colorIndicator', blank=True, null=True)  # Field name made lowercase.
    colors = models.TextField(blank=True, null=True)
    convertedmanacost = models.TextField(db_column='convertedManaCost', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    dueldeck = models.TextField(db_column='duelDeck', blank=True, null=True)  # Field name made lowercase.
    edhrecrank = models.IntegerField(db_column='edhrecRank', blank=True, null=True)  # Field name made lowercase.
    faceconvertedmanacost = models.TextField(db_column='faceConvertedManaCost', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    faceflavorname = models.TextField(db_column='faceFlavorName', blank=True, null=True)  # Field name made lowercase.
    facemanavalue = models.TextField(db_column='faceManaValue', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    facename = models.TextField(db_column='faceName', blank=True, null=True)  # Field name made lowercase.
    finishes = models.TextField(blank=True, null=True)
    flavorname = models.TextField(db_column='flavorName', blank=True, null=True)  # Field name made lowercase.
    flavortext = models.TextField(db_column='flavorText', blank=True, null=True)  # Field name made lowercase.
    frameeffects = models.TextField(db_column='frameEffects', blank=True, null=True)  # Field name made lowercase.
    frameversion = models.TextField(db_column='frameVersion', blank=True, null=True)  # Field name made lowercase.
    hand = models.TextField(blank=True, null=True)
    hasalternativedecklimit = models.IntegerField(db_column='hasAlternativeDeckLimit')  # Field name made lowercase.
    hascontentwarning = models.IntegerField(db_column='hasContentWarning')  # Field name made lowercase.
    hasfoil = models.IntegerField(db_column='hasFoil')  # Field name made lowercase.
    hasnonfoil = models.IntegerField(db_column='hasNonFoil')  # Field name made lowercase.
    isalternative = models.IntegerField(db_column='isAlternative')  # Field name made lowercase.
    isfullart = models.IntegerField(db_column='isFullArt')  # Field name made lowercase.
    isfunny = models.IntegerField(db_column='isFunny')  # Field name made lowercase.
    isonlineonly = models.IntegerField(db_column='isOnlineOnly')  # Field name made lowercase.
    isoversized = models.IntegerField(db_column='isOversized')  # Field name made lowercase.
    ispromo = models.IntegerField(db_column='isPromo')  # Field name made lowercase.
    isrebalanced = models.IntegerField(db_column='isRebalanced')  # Field name made lowercase.
    isreprint = models.IntegerField(db_column='isReprint')  # Field name made lowercase.
    isreserved = models.IntegerField(db_column='isReserved')  # Field name made lowercase.
    isstarter = models.IntegerField(db_column='isStarter')  # Field name made lowercase.
    isstoryspotlight = models.IntegerField(db_column='isStorySpotlight')  # Field name made lowercase.
    istextless = models.IntegerField(db_column='isTextless')  # Field name made lowercase.
    istimeshifted = models.IntegerField(db_column='isTimeshifted')  # Field name made lowercase.
    keywords = models.TextField(blank=True, null=True)
    language = models.TextField(blank=True, null=True)
    layout = models.TextField(blank=True, null=True)
    leadershipskills = models.TextField(db_column='leadershipSkills', blank=True, null=True)  # Field name made lowercase.
    life = models.TextField(blank=True, null=True)
    loyalty = models.TextField(blank=True, null=True)
    manacost = models.TextField(db_column='manaCost', blank=True, null=True)  # Field name made lowercase.
    manavalue = models.TextField(db_column='manaValue', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mcmid = models.TextField(db_column='mcmId', blank=True, null=True)  # Field name made lowercase.
    mcmmetaid = models.TextField(db_column='mcmMetaId', blank=True, null=True)  # Field name made lowercase.
    mtgarenaid = models.TextField(db_column='mtgArenaId', blank=True, null=True)  # Field name made lowercase.
    mtgjsonv4id = models.TextField(db_column='mtgjsonV4Id', blank=True, null=True)  # Field name made lowercase.
    mtgofoilid = models.TextField(db_column='mtgoFoilId', blank=True, null=True)  # Field name made lowercase.
    mtgoid = models.TextField(db_column='mtgoId', blank=True, null=True)  # Field name made lowercase.
    multiverseid = models.TextField(db_column='multiverseId', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(blank=True, null=True)
    number = models.TextField(blank=True, null=True)
    originalprintings = models.TextField(db_column='originalPrintings', blank=True, null=True)  # Field name made lowercase.
    originalreleasedate = models.TextField(db_column='originalReleaseDate', blank=True, null=True)  # Field name made lowercase.
    originaltext = models.TextField(db_column='originalText', blank=True, null=True)  # Field name made lowercase.
    originaltype = models.TextField(db_column='originalType', blank=True, null=True)  # Field name made lowercase.
    otherfaceids = models.TextField(db_column='otherFaceIds', blank=True, null=True)  # Field name made lowercase.
    power = models.TextField(blank=True, null=True)
    printings = models.TextField(blank=True, null=True)
    promotypes = models.TextField(db_column='promoTypes', blank=True, null=True)  # Field name made lowercase.
    purchaseurls = models.TextField(db_column='purchaseUrls', blank=True, null=True)  # Field name made lowercase.
    rarity = models.TextField(blank=True, null=True)
    rebalancedprintings = models.TextField(db_column='rebalancedPrintings', blank=True, null=True)  # Field name made lowercase.
    scryfallid = models.TextField(db_column='scryfallId', blank=True, null=True)  # Field name made lowercase.
    scryfallillustrationid = models.TextField(db_column='scryfallIllustrationId', blank=True, null=True)  # Field name made lowercase.
    scryfalloracleid = models.TextField(db_column='scryfallOracleId', blank=True, null=True)  # Field name made lowercase.
    securitystamp = models.TextField(db_column='securityStamp', blank=True, null=True)  # Field name made lowercase.
    setcode = models.TextField(db_column='setCode', blank=True, null=True)  # Field name made lowercase.
    side = models.TextField(blank=True, null=True)
    signature = models.TextField(blank=True, null=True)
    subtypes = models.TextField(blank=True, null=True)
    supertypes = models.TextField(blank=True, null=True)
    tcgplayeretchedproductid = models.TextField(db_column='tcgplayerEtchedProductId', blank=True, null=True)  # Field name made lowercase.
    tcgplayerproductid = models.TextField(db_column='tcgplayerProductId', blank=True, null=True)  # Field name made lowercase.
    text = models.TextField(blank=True, null=True)
    toughness = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    types = models.TextField(blank=True, null=True)
    uuid = models.TextField(unique=True)
    variations = models.TextField(blank=True, null=True)
    watermark = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cards'


class ForeignData(models.Model):
    flavortext = models.TextField(db_column='flavorText', blank=True, null=True)  # Field name made lowercase.
    language = models.TextField(blank=True, null=True)
    multiverseid = models.IntegerField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    uuid = models.ForeignKey(Cards, models.DO_NOTHING, db_column='uuid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'foreign_data'


class Legalities(models.Model):
    format = models.TextField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)
    uuid = models.ForeignKey(Cards, models.DO_NOTHING, db_column='uuid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'legalities'


class Meta(models.Model):
    date = models.DateField(blank=True, null=True)
    version = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'meta'


class Rulings(models.Model):
    date = models.DateField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    uuid = models.ForeignKey(Cards, models.DO_NOTHING, db_column='uuid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rulings'


class SetTranslations(models.Model):
    language = models.TextField(blank=True, null=True)
    setcode = models.ForeignKey('Sets', models.DO_NOTHING, db_column='setCode', blank=True, null=True)  # Field name made lowercase.
    translation = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'set_translations'


class Sets(models.Model):
    basesetsize = models.IntegerField(db_column='baseSetSize', blank=True, null=True)  # Field name made lowercase.
    block = models.TextField(blank=True, null=True)
    booster = models.TextField(blank=True, null=True)
    code = models.TextField(unique=True)
    isfoilonly = models.IntegerField(db_column='isFoilOnly')  # Field name made lowercase.
    isforeignonly = models.IntegerField(db_column='isForeignOnly')  # Field name made lowercase.
    isnonfoilonly = models.IntegerField(db_column='isNonFoilOnly')  # Field name made lowercase.
    isonlineonly = models.IntegerField(db_column='isOnlineOnly')  # Field name made lowercase.
    ispartialpreview = models.IntegerField(db_column='isPartialPreview')  # Field name made lowercase.
    keyrunecode = models.TextField(db_column='keyruneCode', blank=True, null=True)  # Field name made lowercase.
    mcmid = models.IntegerField(db_column='mcmId', blank=True, null=True)  # Field name made lowercase.
    mcmidextras = models.IntegerField(db_column='mcmIdExtras', blank=True, null=True)  # Field name made lowercase.
    mcmname = models.TextField(db_column='mcmName', blank=True, null=True)  # Field name made lowercase.
    mtgocode = models.TextField(db_column='mtgoCode', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(blank=True, null=True)
    parentcode = models.TextField(db_column='parentCode', blank=True, null=True)  # Field name made lowercase.
    releasedate = models.DateField(db_column='releaseDate', blank=True, null=True)  # Field name made lowercase.
    sealedproduct = models.TextField(db_column='sealedProduct', blank=True, null=True)  # Field name made lowercase.
    tcgplayergroupid = models.IntegerField(db_column='tcgplayerGroupId', blank=True, null=True)  # Field name made lowercase.
    totalsetsize = models.IntegerField(db_column='totalSetSize', blank=True, null=True)  # Field name made lowercase.
    type = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sets'


class Tokens(models.Model):
    artist = models.TextField(blank=True, null=True)
    asciiname = models.TextField(db_column='asciiName', blank=True, null=True)  # Field name made lowercase.
    availability = models.TextField(blank=True, null=True)
    boostertypes = models.TextField(db_column='boosterTypes', blank=True, null=True)  # Field name made lowercase.
    bordercolor = models.TextField(db_column='borderColor', blank=True, null=True)  # Field name made lowercase.
    coloridentity = models.TextField(db_column='colorIdentity', blank=True, null=True)  # Field name made lowercase.
    colors = models.TextField(blank=True, null=True)
    facename = models.TextField(db_column='faceName', blank=True, null=True)  # Field name made lowercase.
    finishes = models.TextField(blank=True, null=True)
    flavortext = models.TextField(db_column='flavorText', blank=True, null=True)  # Field name made lowercase.
    frameeffects = models.TextField(db_column='frameEffects', blank=True, null=True)  # Field name made lowercase.
    frameversion = models.TextField(db_column='frameVersion', blank=True, null=True)  # Field name made lowercase.
    hasfoil = models.IntegerField(db_column='hasFoil')  # Field name made lowercase.
    hasnonfoil = models.IntegerField(db_column='hasNonFoil')  # Field name made lowercase.
    isfullart = models.IntegerField(db_column='isFullArt')  # Field name made lowercase.
    isfunny = models.IntegerField(db_column='isFunny')  # Field name made lowercase.
    ispromo = models.IntegerField(db_column='isPromo')  # Field name made lowercase.
    isreprint = models.IntegerField(db_column='isReprint')  # Field name made lowercase.
    keywords = models.TextField(blank=True, null=True)
    language = models.TextField(blank=True, null=True)
    layout = models.TextField(blank=True, null=True)
    mcmid = models.TextField(db_column='mcmId', blank=True, null=True)  # Field name made lowercase.
    mtgarenaid = models.TextField(db_column='mtgArenaId', blank=True, null=True)  # Field name made lowercase.
    mtgjsonv4id = models.TextField(db_column='mtgjsonV4Id', blank=True, null=True)  # Field name made lowercase.
    multiverseid = models.TextField(db_column='multiverseId', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(blank=True, null=True)
    number = models.TextField(blank=True, null=True)
    originaltext = models.TextField(db_column='originalText', blank=True, null=True)  # Field name made lowercase.
    originaltype = models.TextField(db_column='originalType', blank=True, null=True)  # Field name made lowercase.
    otherfaceids = models.TextField(db_column='otherFaceIds', blank=True, null=True)  # Field name made lowercase.
    power = models.TextField(blank=True, null=True)
    promotypes = models.TextField(db_column='promoTypes', blank=True, null=True)  # Field name made lowercase.
    reverserelated = models.TextField(db_column='reverseRelated', blank=True, null=True)  # Field name made lowercase.
    scryfallid = models.TextField(db_column='scryfallId', blank=True, null=True)  # Field name made lowercase.
    scryfallillustrationid = models.TextField(db_column='scryfallIllustrationId', blank=True, null=True)  # Field name made lowercase.
    scryfalloracleid = models.TextField(db_column='scryfallOracleId', blank=True, null=True)  # Field name made lowercase.
    securitystamp = models.TextField(db_column='securityStamp', blank=True, null=True)  # Field name made lowercase.
    setcode = models.TextField(db_column='setCode', blank=True, null=True)  # Field name made lowercase.
    side = models.TextField(blank=True, null=True)
    signature = models.TextField(blank=True, null=True)
    subtypes = models.TextField(blank=True, null=True)
    supertypes = models.TextField(blank=True, null=True)
    tcgplayerproductid = models.TextField(db_column='tcgplayerProductId', blank=True, null=True)  # Field name made lowercase.
    text = models.TextField(blank=True, null=True)
    toughness = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    types = models.TextField(blank=True, null=True)
    uuid = models.TextField()
    watermark = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tokens'
