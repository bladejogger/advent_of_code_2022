// isn't getting the correct value for the very last line
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

enum MAX_SZ {MAX_TOK = 16, MAX_NAME = 32, MAX_PATH = 128};

struct node
{
    char prior[MAX_PATH]; // path that lead here
    char path[MAX_PATH]; // leading path + here
    long sz;
    struct node *next;
    struct node *prev;
};

struct node * head = NULL;
struct node * HERE = NULL;

void print_list(void)
{
    struct node *cursor = head;
    while (NULL != cursor) {
        if (100000 > (cursor->sz)) {
            printf("%s : %ld\n", cursor->path, cursor->sz);
        }
        cursor = cursor->next;
    }
    puts("list printed");
}

void clear_list(void)
{
    struct node *cursor = head;
    while (NULL != cursor) {
        head = head->next;
        free(cursor);
        cursor = head;
    }
    puts("list emptied");
}

int search_list(char *dir)
{
    int index = 0;
    struct node *cursor = head;
    while (cursor) {
        if (0 == strncmp(cursor->path, dir, MAX_NAME)) {
            return index; // node exists
        }
        index++;
        cursor = cursor->next;
    }
    return -1; // new node
}

void new_node(char *prior, char *full, unsigned int size)
{
    struct node * link = (struct node *)calloc(sizeof(struct node), 1);
    if (NULL == HERE) {
        head = link;
        HERE = head;
    }
    else {
        struct node * cur = HERE;
        while (NULL != cur->next) {
            cur = cur->next;
        }
        cur->next = link;
        link->prev = cur;
    }
    if (NULL == strncpy(link->prior, prior, MAX_PATH)) {
        printf("yoooo can't copy this path, brah: %s\n", prior);
        return;
    }
    if (NULL == strncpy(link->path, full, MAX_PATH)) {
        printf("yoooo can't copy this path, brah: %s\n", full);
        return;
    }
    link->sz = size;
    HERE = link;
    //printf("in new node:\nHERE path: %s\n", HERE->prior);
    //printf("in new node:\nHERE path: %s\n", HERE->path);
}

// TODO: return path len and err check
void get_paths(char *prior_path_holder, char *full_path_holder, char *new_dir)
{
    //printf("gull path start: %s\n", new_dir);
    char * slash = "/";
    if (NULL == head) {
        strncpy(prior_path_holder, new_dir, 1);
        strncpy(full_path_holder, new_dir, 1);
    }
    else if (NULL == head->next) {
        strncpy(prior_path_holder, slash, 1);
        //
        strncpy(full_path_holder, slash, 1);
        strncat(full_path_holder, new_dir, MAX_NAME);
        strncat(full_path_holder, slash, 1);
    }
    else {
        strncpy(prior_path_holder, HERE->path, MAX_PATH);
        //
        strncpy(full_path_holder, HERE->path, MAX_PATH);
        strncat(full_path_holder, new_dir, MAX_NAME);
        strncat(full_path_holder, slash, 1);
    }
}

// maybe err check this?
void move_here(int index)
{
    HERE = head;
    while (0 < index) {
        HERE = HERE->next;
        index--;
    }
}

int main(int argc, char *argv[])
{
    int ret = 0;

    if (2 != argc) {
        fprintf(stderr, "yoooo only 2 args, brah\n");
        ret = 1;
        goto cleanup_0;
    }

    FILE *fp= fopen(argv[1], "r");
    if (NULL == fp) {
        fprintf(stderr, "yoooo can't open your file, brah\n");
        ret = 2;
        goto cleanup_0;
    }

    long dir_sz = 0;
    long file_sz = 0;
    char buf[MAX_NAME] = {'\0'};
    char *token = NULL;
    char *end;
    char * list = "ls";
    char * cdir = "cd";
    const char *delim = " \n";
    while (NULL != fgets(buf, MAX_NAME - 1, fp)) {
        int cmd_flag = 0;
        token = strtok(buf, delim);
        while (NULL != token) {
            if (cmd_flag) {
                if (0 == strncmp(list,  token, 2)) {
                    goto danger_end;
                }
                // this caused an error earlier... was catching a dir name
                else if (0 == strncmp(cdir, token, 2)) { // here for vis
                    goto danger_end;
                }
                // index of 'dir' in list to move to
                int x = 0;
                // move up a dir: above node must exist
                if (0 == strncmp("..", token, 3)) {
                    if (0 == HERE->sz) {
                        HERE->sz = dir_sz;
                    }
                    x = search_list(HERE->prior);
                    move_here(x);
                    dir_sz = 0;
                }
                // move down a dir
                // / = 11534419 ccjp = 328708 mbtsvblj = 653774
                else {
                    char path[MAX_PATH] = {'\0'};
                    char full_path[MAX_PATH] = {'\0'};
                    get_paths(path, full_path, token);
                    x = search_list(full_path);
                    // node exists
                    if (-1 < x) {
                        if (0 == HERE->sz) {
                            HERE->sz = dir_sz;
                        }
                        move_here(x);
                        dir_sz = 0;
                    }
                    // create new node
                    else {
                        if (HERE && (0 == HERE->sz)) {
                            HERE->sz = dir_sz;
                        }
                        dir_sz = 0;
                        new_node(path, full_path, dir_sz);
                    }
                    //printf("HERE path = %s\n", HERE->path);
                }
            }
            else {
                // incoming command in next token
                if (0 == strncmp("$", token, 1)) {
                    //update_dir_size(dir_sz);
                    cmd_flag++;
                }
                // 'dir' found in output of 'ls' cmd // here for vis
                else if (0 == strncmp("dir", token, 3)) {
                    //printf("%s ", token);
                    goto danger_end;
                }
                // received file size numbers
                else if (token[0] > 47 && token[0] <58) {
                    file_sz = strtol(token, &end, 10);
                    dir_sz += file_sz;
                }
                // is a file name, which we don't do anything w
                else {
                    goto danger_end;
                }
            }
danger_end:
            token = strtok(NULL, delim);
        }
        memset(buf, '\0', MAX_NAME);
    }

    if (head) {
        print_list();
        clear_list();
        head = NULL;
        HERE = NULL;
    }

    fclose(fp);
    fp = NULL;
cleanup_0:
    return ret;
}
