import xmlschema


def validate_xml_with_schema(xml_data, xml_schema):
    try:
        xmlschema.validate(xml_data.data.decode(), xml_schema.data.decode())
    except xmlschema.XMLSchemaException as error:
        print("Failed to fetch data", error)
        return "Failed"
    return


