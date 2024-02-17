import psycopg2
import psycopg2.extras
import xml.etree.ElementTree as ET

conn = psycopg2.connect(
    database="postgres",
    host="database-1.cov4jvuitnep.us-east-1.rds.amazonaws.com",
    user="postgres",
    password="mhatre123",
    port="5432")


def getCur():
    return conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)


def get_losscost_zip(pclass, zip):
    cursor = getCur()
    cursor.execute("SELECT p1,p2,p3,p4,p5,p6,p7,p8,p9,earthquake,hurricane FROM rating.losscost_zip where protection_class=%s and zip=%s",
                   (pclass, zip))
    row = cursor.fetchone()
    data = {"p1": 1, "p2": 1, "p3": 1, "p4": 1, "p5": 1, "p6": 1, "p7": 1, "p8": 1, "p9": 1 , "earthquake" : 1 , "hurricane" : 1 }
    cursor.close()
    if row is None:
        return data
    return row


def get_losscost(pclass, county, censustrack, censusblock):
    cursor = getCur()
    cursor.execute(
        "SELECT p1,p2,p3,p4,p5,p6,p7,p8,p9,earthquake,hurricane FROM rating.losscost where protection_class=%s and county=%s and census_track=%s and census_block=%s",
        (pclass, county, censustrack, censusblock))
    row = cursor.fetchone()
    data = {"p1": 1, "p2": 1, "p3": 1, "p4": 1, "p5": 1, "p6": 1, "p7": 1, "p8": 1, "p9": 1 , "earthquake" : 1 , "hurricane" : 1 }
    cursor.close()
    if row is None:
        return data
    return row


def get_lcm():
    cursor = getCur()
    cursor.execute("SELECT p1,p2,p3,p4,p5,p6,p7,p8,p9,earthquake,hurricane FROM rating.lcm where id = 1")
    row = cursor.fetchone()
    data = {"p1": 1, "p2": 1, "p3": 1, "p4": 1, "p5": 1, "p6": 1, "p7": 1, "p8": 1, "p9": 1 , "earthquake" : 1 , "hurricane" : 1 }
    cursor.close()
    if row is None:
        return data
    return row


def get_aoi_factor(limit):
    cursor = getCur()
    cursor.execute("SELECT p1,p2,p3,p4,p5,p6,p7,p8,p9,earthquake,hurricane FROM rating.aoi_factor where cov_limit = %s", (limit,))
    row = cursor.fetchone()
    data = {"p1": 1, "p2": 1, "p3": 1, "p4": 1, "p5": 1, "p6": 1, "p7": 1, "p8": 1, "p9": 1 , "earthquake" : 1 , "hurricane" : 1 }
    cursor.close()
    if row is None:
        return data
    return row


def get_aop_ded_factor(deductible):
    cursor = getCur()
    cursor.execute("SELECT p1,p2,p3,p4,p5,p6,p7,p8,p9,earthquake,hurricane FROM rating.aop_ded_factor where deductible = %s", (deductible,))
    row = cursor.fetchone()
    data = {"p1": 1, "p2": 1, "p3": 1, "p4": 1, "p5": 1, "p6": 1, "p7": 1, "p8": 1, "p9": 1 , "earthquake" : 1 , "hurricane" : 1 }
    cursor.close()
    if row is None:
        return data
    return row


def get_wind_ded_factor(deductible):
    cursor = getCur()
    cursor.execute("SELECT p1,p2,p3,p4,p5,p6,p7,p8,p9,earthquake,hurricane FROM rating.wind_ded_factor where deductible = %s", (deductible,))
    row = cursor.fetchone()
    data = {"p1": 1, "p2": 1, "p3": 1, "p4": 1, "p5": 1, "p6": 1, "p7": 1, "p8": 1, "p9": 1 , "earthquake" : 1 , "hurricane" : 1 }
    cursor.close()
    if row is None:
        return data
    return row

def get_constr_age_factor(age):
    cursor = getCur()
    cursor.execute("SELECT p1,p2,p3,p4,p5,p6,p7,p8,p9,earthquake,hurricane FROM rating.age_of_construction_factor where age = %s", (age,))
    row = cursor.fetchone()
    data = {"p1": 1, "p2": 1, "p3": 1, "p4": 1, "p5": 1, "p6": 1, "p7": 1, "p8": 1, "p9": 1 , "earthquake" : 1 , "hurricane" : 1 }
    cursor.close()
    if row is None:
        return data
    return row

def get_constr_type_factor(pclass , const_type):
    cursor = getCur()
    cursor.execute("SELECT p1,p2,p3,p4,p5,p6,p7,p8,p9,earthquake,hurricane FROM rating.protection_class_cons_type_factor where construction_type = %s and protection_class = %s", (pclass,const_type))
    row = cursor.fetchone()
    data = {"p1": 1, "p2": 1, "p3": 1, "p4": 1, "p5": 1, "p6": 1, "p7": 1, "p8": 1, "p9": 1 , "earthquake" : 1 , "hurricane" : 1 }
    cursor.close()
    if row is None:
        return data
    return row

def get_territory(policy, prop, zip):
    cursor = getCur()
    cursor.execute("SELECT territory FROM rating.zip_territory where zip=%s", (zip,))
    row = cursor.fetchone()
    data = 1
    cursor.close()
    if row is None:
        return data
    data = row["territory"]
    return data


def rate(policy: ET):
    data = {}
    for prop in policy.findall('./property'):
        zip = prop.find('./address/zip').text
        terr = get_territory(policy, prop, zip)
        add = prop.find('./address')
        add.append(getElement('territory', terr))
    pclass = policy.find('./property/protectionclass').text
    age_const = policy.find('./property/construction/age').text
    const_type = policy.find('./property/construction/type').text
    county = policy.find('./property/address/county').text
    censustrack = policy.find('./property/address/censustrack').text
    censusblock = policy.find('./property/address/censusblock').text
    zipcode = policy.find('./property/address/zip').text

    data["pclass"] = pclass
    data["age_const"] = age_const
    data["const_type"] = const_type
    data["county"] = county
    data["censustrack"] = censustrack
    data["censusblock"] = censusblock
    data["zipcode"] = zipcode

    polPrem = 0

    for cov in policy.findall('./coverages/coverage[code="A"]'):
        limit = cov.find('./limit').text
        deductible = cov.find('./deductible').text
        winddeductible = cov.find('./winddeductible').text
        cov_premium = 0
        perils = cov.find('./perils')
        for peril in perils.findall('./peril'):
            code = peril.find('./code').text

            premium = calCovPrem(data, peril, limit, deductible, winddeductible, code)

            cov_premium += premium
            peril.append(getElement('premium', round(premium, 2)))

        earthquake_yn = cov.find('./earthquake').text
        if earthquake_yn == "Y":
            code = "earthquake"
            peril = getElement('peril', None)
            peril.append(getElement("code",code))
            premium = calCovPrem(data, peril, limit, deductible, winddeductible, code)
            perils.append(peril)
            cov_premium += premium
            peril.append(getElement('premium', round(premium, 2)))

        hurricane_yn = cov.find('./hurricane').text
        if hurricane_yn == "Y":
            code = "hurricane"
            peril = getElement('peril', None)
            peril.append(getElement("code", code))
            premium = calCovPrem(data, peril, limit, deductible, winddeductible, code)
            perils.append(peril)
            cov_premium += premium
            peril.append(getElement('premium', round(premium, 2)))

        polPrem += cov_premium
        cov.append(getElement('premium', round(cov_premium, 2)))
    policy.append(getElement('premium', round(polPrem, 2)))
    return policy


def calCovPrem (data, peril, limit, deductible, winddeductible, code):
    # losscost = get_losscost(pclass, county, censustrack, censusblock)[code]
    losscost_zip = get_losscost_zip(data["pclass"], data["zipcode"])[code]
    peril.append(getElement('losscost', losscost_zip))

    lcm = get_lcm()[code]
    peril.append(getElement('lcm', lcm))

    aoi = get_aoi_factor(limit)[code]
    peril.append(getElement('aoi', aoi))

    aop_ded = get_aop_ded_factor(deductible)[code]
    peril.append(getElement('aopded', aop_ded))

    wind_ded = get_wind_ded_factor(winddeductible)[code]
    peril.append(getElement('windded', wind_ded))

    hurr_ded = 1.0
    peril.append(getElement('hurrded', hurr_ded))

    age_factor = get_constr_age_factor(data["age_const"])[code]
    peril.append(getElement('age_factor', age_factor))

    const_type_factor = get_constr_type_factor(data["pclass"], data["const_type"])[code]
    peril.append(getElement('const_type_factor', const_type_factor))

    fit_tier = 1.0
    peril.append(getElement('credit_policy_tier', fit_tier))

    multiple_family = 1.0
    peril.append(getElement('multiple_family', multiple_family))

    town_house = 1.0
    peril.append(getElement('town_house', town_house))

    seasonal_property = 1.10
    peril.append(getElement('seasonal_property', seasonal_property))

    roof_type = 1.0
    peril.append(getElement('roof_type', roof_type))

    no_of_stories = 1.0
    peril.append(getElement('no_of_stories', no_of_stories))

    square_footage = 1.0
    peril.append(getElement('square_footage', square_footage))

    basic_premium = (losscost_zip * lcm * aoi * aop_ded * wind_ded * hurr_ded * age_factor *
                     fit_tier * multiple_family * town_house * seasonal_property * roof_type *
                     no_of_stories * square_footage
                     )

    peril.append(getElement('basic_premium', basic_premium))

    spcl_pers_prop_cov = 1.0
    peril.append(getElement('spcl_pers_prop_cov', spcl_pers_prop_cov))

    loss_settlement = 1.0
    peril.append(getElement('loss_settlement', loss_settlement))

    specified_addl_amt = 1.0
    peril.append(getElement('specified_addl_amt', specified_addl_amt))

    cov_d_loss_of_use = 1.0
    peril.append(getElement('cov_d_loss_of_use', cov_d_loss_of_use))

    home_alert = 1.0
    peril.append(getElement('home_alert', home_alert))

    claim_record = 1.0
    peril.append(getElement('claim_record', claim_record))

    bldg_ordnc = 1.0
    peril.append(getElement('bldg_ordnc', bldg_ordnc))

    bldr_discount = 1.0
    peril.append(getElement('bldr_discount', bldr_discount))

    home_auto = 1.0
    peril.append(getElement('home_auto', home_auto))

    emp_discount = 1.0
    peril.append(getElement('emp_discount', emp_discount))

    new_home = 1.0
    peril.append(getElement('new_home', new_home))

    solid_fuel_device = 1.0
    peril.append(getElement('solid_fuel_device', solid_fuel_device))

    sup_constr = 1.0
    peril.append(getElement('sup_constr', sup_constr))

    windstorm_mitg = 1.0
    peril.append(getElement('windstorm_mitg', windstorm_mitg))

    companion_disc = 1.0
    peril.append(getElement('companion_disc', companion_disc))

    ins_age_dis = 1.0
    peril.append(getElement('ins_age_dis', ins_age_dis))

    pers_status = 1.0
    peril.append(getElement('ins_age_dis', ins_age_dis))

    acv_roof = 1.0
    peril.append(getElement('acv_roof', acv_roof))

    gated_comm = 1.0
    peril.append(getElement('gated_comm', gated_comm))

    sevr_back_disc = 1.0
    peril.append(getElement('sevr_back_disc', sevr_back_disc))

    pers_liab_limit = 1.0
    peril.append(getElement('pers_liab_limit', pers_liab_limit))

    med_pay_limit = 1.0
    peril.append(getElement('med_pay_limit', med_pay_limit))

    pers_inj_cove = 1.0
    peril.append(getElement('pers_inj_cove', pers_inj_cove))

    animal_liab_buybk = 1.0
    peril.append(getElement('animal_liab_buybk', animal_liab_buybk))

    peril_mod = 1.0
    peril.append(getElement('peril_mod', peril_mod))

    premium = (basic_premium * spcl_pers_prop_cov * loss_settlement * specified_addl_amt *
               cov_d_loss_of_use * home_alert * claim_record * bldg_ordnc * bldr_discount *
               home_auto * emp_discount * new_home * solid_fuel_device * sup_constr * windstorm_mitg *
               companion_disc * ins_age_dis * pers_status * acv_roof * gated_comm * sevr_back_disc *
               pers_liab_limit * med_pay_limit * pers_inj_cove * animal_liab_buybk * peril_mod
               )
    return premium;

def getElement (name, value):
    if value is not None:
        ele = ET.Element(name)
        ele.text = str(value)
        return ele
    else:
        ele = ET.Element(name)
        return ele