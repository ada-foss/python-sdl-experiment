#include <stdlib.h>
#include <SDL2/SDL.h>
//#include "SDL.h"
#include "viewport.h"

void c_square(int n, double *array_in, double *array_out)
{ //return the square of array_in of length n in array_out
    int i;

    for (i = 0; i < n; i++)
    {
        array_out[i] = array_in[i] * array_in[i];
    }
}

Application* initSDL(int *errorcode, int screen_width, int screen_height) {
    int rendererFlags, windowFlags;
    Application *app = malloc(sizeof(Application));
    if (!app)
    {
        *errorcode = 1;
        return 0;
    }

    rendererFlags = SDL_RENDERER_ACCELERATED;
    windowFlags = 0;
    app->window = SDL_CreateWindow("Shooter 01", SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED, screen_width, screen_height, windowFlags);
    
    if (!app->window)
    {
        *errorcode = 2;
        return 0;
    }

    SDL_SetHint(SDL_HINT_RENDER_SCALE_QUALITY, "linear");
    app->renderer = SDL_CreateRenderer(app->window, -1, rendererFlags);

    if (!app->renderer)
    {
        *errorcode = 3;
        return 0;
    }

    return app;
}
