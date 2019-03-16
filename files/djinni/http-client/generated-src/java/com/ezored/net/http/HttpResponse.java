// AUTOGENERATED FILE - DO NOT MODIFY!
// This file generated by Djinni from proj.djinni

package com.ezored.net.http;

import java.util.ArrayList;

public final class HttpResponse {


    /*package*/ final int mCode;

    /*package*/ final String mBody;

    /*package*/ final ArrayList<HttpHeader> mHeaders;

    public HttpResponse(
            int code,
            String body,
            ArrayList<HttpHeader> headers) {
        this.mCode = code;
        this.mBody = body;
        this.mHeaders = headers;
    }

    public int getCode() {
        return mCode;
    }

    public String getBody() {
        return mBody;
    }

    public ArrayList<HttpHeader> getHeaders() {
        return mHeaders;
    }

    @Override
    public String toString() {
        return "HttpResponse{" +
                "mCode=" + mCode +
                "," + "mBody=" + mBody +
                "," + "mHeaders=" + mHeaders +
        "}";
    }

}