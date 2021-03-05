import base64
import psycopg2
import json
from types import SimpleNamespace


def block_ready_receiver(event, context):
    """Triggered from a message on a Cloud Pub/Sub topic.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    blockreadymsg = json.loads(pubsub_message, object_hook=lambda d: SimpleNamespace(**d))
    print(blockreadymsg.eventId, blockreadymsg.eventType, blockreadymsg.sourceSystemId, blockreadymsg.sourceSystemName,
          blockreadymsg.dataServiceVersionUri,
          blockreadymsg.snapshotContextTypeCode, blockreadymsg.blockLabel, blockreadymsg.blockVersion,
          blockreadymsg.dataUri,
          blockreadymsg.metadataUri)
    query = "INSERT INTO block_ready_sh (eventId,eventType,sourceSystemId,sourceSystemName,dataServiceVersionUri," \
            "snapshotContextTypeCode,blockLabel,blockVersion,dataUri,metadataUri) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s," \
            "%s); "
    data = (
        blockreadymsg.eventId, blockreadymsg.eventType, blockreadymsg.sourceSystemId, blockreadymsg.sourceSystemName,
        blockreadymsg.dataServiceVersionUri, blockreadymsg.snapshotContextTypeCode, blockreadymsg.blockLabel,
        blockreadymsg.blockVersion, blockreadymsg.dataUri, blockreadymsg.metadataUri)
    conn = psycopg2.connect(host="*******", port=5432, database="*****", user="*****",
                            password="********")
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute(query, data)
    conn.commit()
    print("Records inserted........")
    #cur.execute("""SELECT * FROM *****""")
    #query_results = cur.fetchall()
    #print(query_results)
    cur.close()
    conn.close()
