from yilongwang import  publicMians as PM;
import redis


"""*******状态码中间层******"""
class CodeStatusMiddleware(object):
    def process_response(self, response, request, spider):
        if response.status == 200:
            PM.getCorlor('==> <200>访问正常.','',1,40,42);
            return response
        elif response.status == 429:
            PM.getCorlor('==> <429>请求失败！','',1,40,41);
            PM.getPrint('==> 请求太过频繁！','',31);
            redisdb = redis.Redis(host='192.168.0.102', port=6379, db=0, decode_responses='true');
            redisdb.lpush('except_urls:urls',response.url)
            return response
        elif response.status == 403:
            PM.getCorlor('==> <403>请求失败！','',1,40,41);
            PM.getPrint('==> 请求被拒绝！','',31);
            return response


        elif response.status == "503 Service Unavailable":

            PM.getCorlor('==> <503>请求失败', '', 1, 40, 41);

            PM.getPrint('==> 服务器维护或容量不足！', '', 31);

            return response

        else:
            return response








