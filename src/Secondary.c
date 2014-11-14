#include <jni.h>
#include <stdlib.h>
#include <stdio.h>
#include "Secondary.h"

jdouble memAccess=0;

void swap(jint *array, jint pos1, jint pos2) {
  memAccess+=6;
  jint temp=*(array+pos1);
  *(array+pos1)=*(array+pos2);
  *(array+pos2)=temp;
}

JNIEXPORT void JNICALL Java_Secondary_sort(JNIEnv *env, jobject obj, jintArray array) {
  memAccess+=7;
  jsize elements=(*env)->GetArrayLength(env,array);
  jint *arr=(*env)->GetIntArrayElements(env,array,0);
  jint i,j;
  for (i=1;i<elements;i++) {
    for (j=i;j>0;j--) {
      if (*(arr+j)>=*(arr+(j-1))) {
	memAccess+=8;
	break;
      }
      else {
	swap(arr,j,j-1);
      }
    }
  }
  (*env)->ReleaseIntArrayElements(env,array,arr,0);
}

JNIEXPORT jdouble JNICALL Java_Secondary_getMemAccess (JNIEnv *env, jobject obj) {
  return memAccess;
}


