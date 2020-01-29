import requests, bs4, json, os, sys
url = 'https://www.linkedin.com/voyager/api/feed/comments'

arr = sys.argv[1].split('-')
post = arr[-3]+':'+arr[-2]

set = {''}
if os.path.exists('commentersMiniProfile.txt'):
    os.remove('commentersMiniProfile.txt')
file = open('commentersMiniProfile.txt', 'a+')
totalcount = 1
start = 0
loop = 100
while start<totalcount:
    response = requests.get(url, 
                   headers={
'accept-encoding':'gzip, deflate, br',
'accept-language':'en-US,en;q=0.9',
'cookie':'visit="v=1&G"; liap=true; _ga=GA1.2.530301469.1546617336; AMCVS_14215E3D5995C57C0A495C55%40AdobeOrg=1; aam_uuid=24023768278548007684421754200784231300; spectroscopyId=73a6a4d0-41d0-4164-9fe0-cbc83ff1b1a1; lil-lang=en_US; utag_main=v_id:016cd62ca052001c205074ffb5f303073003d06b0086e$_sn:2$_se:2$_ss:0$_st:1570599339161$vapi_domain:linkedin.com$ses_id:1570597492253%3Bexp-session$_pn:1%3Bexp-session; SID=e45f954c-8c72-4747-b275-5063061d5ead; VID=V_2019_10_09_05_3620058; ELOQUA=GUID=A0E2B86784C74EBE9F963B5EAD7F23B5; li_sugr=dfc0219f-886a-47a1-95ed-e18ab3c87d86; _guid=1268eeb2-5c72-4c2f-8a5c-9a9ec4a100c2; lang=v=2&lang=en-US; PLAY_LANG=en; PLAY_SESSION=eyJhbGciOiJIUzI1NiJ9.eyJkYXRhIjp7InNlc3Npb25faWQiOiIyNmU3ZTkwOC01OTlmLTQwMWMtOTVlMy04ZGZiYWExNWM0NjB8MTU3ODQwODE4NiIsInJlY2VudGx5LXNlYXJjaGVkIjoiIiwicmVmZXJyYWwtdXJsIjoiaHR0cHM6Ly93d3cubGlua2VkaW4uY29tL2luL3RoYWxsYWRhc2Fpa3VtYXIvZWRpdC9lZHVjYXRpb24vNjMwODgxNjEzLyIsImFpZCI6IiIsIlJOVC1pZCI6InwwIiwicmVjZW50bHktdmlld2VkIjoiODYyMzYiLCJDUFQtaWQiOiJZVEZqWXpnNE1HTXRZelUyTUMwME9UVTFMV0kyWmpZdFptSmxaR0UzT0RSa01UZzEiLCJleHBlcmllbmNlIjoiZW50aXR5IiwiaXNfbmF0aXZlIjoiZmFsc2UiLCJ3aGl0ZWxpc3QiOiJ7fSIsInRyayI6IiJ9LCJuYmYiOjE1Nzg0MDgxODgsImlhdCI6MTU3ODQwODE4OH0.GS36rRoltlIcsDTp6yer423F4hnNf10OSpSxAEge_E8; bcookie=v=2&fcf53cd0-6f87-4f8b-868a-d450a070f121; bscookie=v=1&2018052010413868f18f32-c93d-44a2-8683-599b91aab4f6AQEhR3jDN7LbjQUW0zRF9qbX2VbN-9zG; lissc=1; li_at=AQEDARG9uIMCRdtfAAABbP-JH4IAAAFwDUklNlEATc19ag2KyteoCCuKTtfj-FXa2vgTILpVdtopHm7PWnxt8GlUbeYaFqUsg61UsjVYMM7OoZoOsXy9_ewRNZ7Xdsw92hOvlGMjbbOuVo0sWSDOIosX; JSESSIONID="ajax:1958595828725120037"; sdsc=1%3A1SZM1shxDNbLt36wZwCgPgvN58iw%3D; _lipt=CwEAAAFv7i8ptJLvjGaHoVI1mF12pZCeEBa5JeXfDWaY_YkRXQb8mzQIuJwv9MK68SDtwyAM_zLAaFHSEzMXefsug38pF7I15a5pr6ZQapovo6ny0jTsfkpftvz1f9fdMrPtKcc4Ec725nqxnMwgLWSi7f3nPXHS3Yz_9VTCmk5TcchL_5h3a8S9PA3HwWgXgOASrFP68BnQzeQrJm9jh5eQH9AlR1tzXdmdhqu8htm2AAuRJekj-lk9m8pm9LRzp2BDOSYxJ_2LNHao59yFBBD9IpRmHiv63nXeL0G4z6CU1mQbtZC9CrqfOy9te65c1dxJE8Har-f2q6g75gpok4iKZyKqq1mXUqTQ-IpHoC-9uyk4d_i2aZm2HkLLGgjslX7lWys8rzBlKBt0T3-P_6pKQ9yXN442m0WZW2LjJmOTH2T3ogZftNfzyy8HBX80yjLB; AMCV_14215E3D5995C57C0A495C55%40AdobeOrg=-1303530583%7CMCIDTS%7C18289%7CMCMID%7C24212079078723226354436631913597708367%7CMCAAMLH-1580853867%7C7%7CMCAAMB-1580853867%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1580256267s%7CNONE%7CvVersion%7C3.3.0%7CMCCIDH%7C404206177; li_oatml=AQHggftxGBSCHgAAAW_vl2btsh3JrltfxgyqKivO8ina4VtWsM0n9h5YP9mdwvWsl0V4HL52NsLfWWAAdKFh121L1b9wTJWL; UserMatchHistory=AQIwcR0mMZSyLAAAAW_yirxN7_3Dm4NTH8JRKXI19EutTQkvyaPrT_B4tMnrXDIVIMOLiCrdscUlmuQbClWcQ0KNgUPiMJsrD3SV33Cg4LF752xDxdg1m-n8UtjSMs0KyjiPBzFtWyKakQKC36TJHxj1KvuMbetTIRaDTjc18uLxlHDOz9f8Oizu5zNiX0lq63RbgaKqa-K34yJuL_XCC6PRIKdzKTvj; lidc="b=SB11:g=123:u=328:i=1580322177:t=1580387073:s=AQEUc3jdiG7X2bp3mWBZv-iC8-zx-B6R"',
'csrf-token':'ajax:1958595828725120037'
},
                   params={
                        'count':100,
                           'q':'comments',
                           'sortOrder':'RELEVANCE',
                           'start':start,
                           'updateId':post})
    data = response.text
    jsonData = json.loads(response.text)
    
    totalcount = jsonData['paging']['total']
    if (totalcount - start) < 100:
        loop = totalcount-start

    for i in range(loop):
        publicIdentifier = jsonData['elements'][i]['commenter']['com.linkedin.voyager.feed.MemberActor']['miniProfile']['publicIdentifier']
        if not set.__contains__(publicIdentifier):
            set.add(publicIdentifier)
            file.write(str(jsonData['elements'][i]['commenter']['com.linkedin.voyager.feed.MemberActor']['miniProfile']))
            file.write('\n')
    start = start+100
    
    
file.close()